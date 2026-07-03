"""
Generate a CG LAMMPS data file for C60 fullerenes on an FCC lattice.
Each C60 is represented as a single bead with mass = 60 * 12.011 g/mol.
Uses the LJ equilibrium distance as the FCC nearest-neighbour spacing.

Usage: python gen_cg_data.py
Output: cg_c60.data
"""
import numpy as np

# ------------------------------------------------------------------
# LJ parameters from PMF fit (lj_fit_parameters.txt)
# ------------------------------------------------------------------
epsilon = 0.43745371   # eV
sigma   = 9.41822741   # Angstroms

# FCC nearest-neighbour distance = LJ minimum = 2^(1/6) * sigma
r_nn    = 2.0**(1.0/6.0) * sigma          # ~10.574 Ang
# FCC lattice parameter: a = r_nn * sqrt(2)
a_fcc   = r_nn * np.sqrt(2.0)             # ~14.950 Ang

n_rep = 3              # 3 x 3 x 3 supercell  →  4 * 27 = 108 beads

# ------------------------------------------------------------------
# Build FCC positions
# ------------------------------------------------------------------
basis = np.array([[0.0, 0.0, 0.0],
                  [0.5, 0.5, 0.0],
                  [0.5, 0.0, 0.5],
                  [0.0, 0.5, 0.5]])

positions = []
for ix in range(n_rep):
    for iy in range(n_rep):
        for iz in range(n_rep):
            for b in basis:
                pos = (np.array([ix, iy, iz]) + b) * a_fcc
                positions.append(pos)
positions = np.array(positions)
N  = len(positions)          # 108
Lx = Ly = Lz = n_rep * a_fcc

mass_C60 = 60.0 * 12.011    # g/mol

print(f"Number of CG beads   : {N}")
print(f"FCC lattice parameter: {a_fcc:.4f} Ang")
print(f"Nearest-neighbour    : {r_nn:.4f} Ang  (= LJ r_min)")
print(f"Box size             : {Lx:.4f} Ang  ({Lx/2:.4f} half)")
print(f"Mass per bead        : {mass_C60:.3f} g/mol")

# ------------------------------------------------------------------
# Write LAMMPS data file  (atom_style full)
# ------------------------------------------------------------------
with open("cg_c60.data", "w") as f:
    f.write("LAMMPS CG data file: C60 beads on FCC lattice\n\n")
    f.write(f"{N} atoms\n")
    f.write("1 atom types\n\n")
    f.write(f"0.000000 {Lx:.6f} xlo xhi\n")
    f.write(f"0.000000 {Ly:.6f} ylo yhi\n")
    f.write(f"0.000000 {Lz:.6f} zlo zhi\n\n")
    f.write("Masses\n\n")
    f.write(f"1 {mass_C60:.4f}  # C60 bead\n\n")
    f.write("Atoms  # full\n\n")
    for i, pos in enumerate(positions):
        # atom-ID  mol-ID  atom-type  charge  x  y  z
        f.write(f"{i+1:5d}  {i+1:5d}  1  0.0"
                f"  {pos[0]:14.6f}  {pos[1]:14.6f}  {pos[2]:14.6f}\n")

print("Written: cg_c60.data")
