"""
Generate an all-atom LAMMPS data file for 108 C60 fullerenes on an FCC lattice.
Uses the single-C60 geometry from ../c60_pair_wo_bonds.data (atoms 1-60).
All molecules share the same orientation; thermal motion randomises them.

Usage: python gen_aa_multi_data.py
Output: aa_c60_108.data
"""
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
template_file = os.path.join(script_dir, "../c60_pair_wo_bonds.data")

# ------------------------------------------------------------------
# Read single C60 template (atoms 1-60)
# ------------------------------------------------------------------
template_atoms = []
in_atoms = False
with open(template_file) as fh:
    for line in fh:
        stripped = line.strip()
        if stripped.startswith("Atoms"):
            in_atoms = True
            continue
        if in_atoms:
            if stripped.startswith("Bonds") or stripped.startswith("Angles") or stripped.startswith("Velocities"):
                break
            if stripped == "":
                continue   # skip blank lines within the Atoms section
            parts = stripped.split()
            if len(parts) >= 7:
                try:
                    atom_id = int(parts[0])
                except ValueError:
                    continue
                if atom_id <= 60:
                    # format: atom-ID mol-ID type charge x y z
                    x, y, z = float(parts[4]), float(parts[5]), float(parts[6])
                    template_atoms.append([x, y, z])

template_atoms = np.array(template_atoms)  # shape (60, 3)
assert len(template_atoms) == 60, f"Expected 60 atoms, got {len(template_atoms)}"

# Centre at origin
com = template_atoms.mean(axis=0)
template_atoms -= com
print(f"C60 template COM (should be ~0): {template_atoms.mean(axis=0)}")
print(f"C60 radius (max dist from COM): {np.linalg.norm(template_atoms, axis=1).max():.3f} Ang")

# ------------------------------------------------------------------
# FCC lattice  (same lattice parameter as the CG run: a_fcc ~ 14.95 Ang)
# ------------------------------------------------------------------
sigma   = 9.41822741   # Ang  (LJ fit)
r_nn    = 2.0**(1.0/6.0) * sigma
a_fcc   = r_nn * np.sqrt(2.0)       # ~14.950 Ang
n_rep   = 3

basis = np.array([[0.0, 0.0, 0.0],
                  [0.5, 0.5, 0.0],
                  [0.5, 0.0, 0.5],
                  [0.0, 0.5, 0.5]])

mol_centers = []
for ix in range(n_rep):
    for iy in range(n_rep):
        for iz in range(n_rep):
            for b in basis:
                pos = (np.array([ix, iy, iz]) + b) * a_fcc
                mol_centers.append(pos)

mol_centers = np.array(mol_centers)
N_mol = len(mol_centers)       # 108
N_atom = N_mol * 60
Lx = Ly = Lz = n_rep * a_fcc

print(f"\nNumber of C60 molecules: {N_mol}")
print(f"Total atoms            : {N_atom}")
print(f"FCC lattice parameter  : {a_fcc:.4f} Ang")
print(f"Box dimensions         : {Lx:.4f} Ang")

# ------------------------------------------------------------------
# Write LAMMPS data file  (atom_style full)
# ------------------------------------------------------------------
with open("aa_c60_108.data", "w") as f:
    f.write("LAMMPS all-atom data file: 108 C60 fullerenes on FCC lattice\n\n")
    f.write(f"{N_atom} atoms\n")
    f.write("1 atom types\n\n")
    f.write(f"0.000000 {Lx:.6f} xlo xhi\n")
    f.write(f"0.000000 {Ly:.6f} ylo yhi\n")
    f.write(f"0.000000 {Lz:.6f} zlo zhi\n\n")
    f.write("Masses\n\n")
    f.write("1 12.0110  # C\n\n")
    f.write("Atoms  # full\n\n")
    atom_global_id = 0
    for mol_id, center in enumerate(mol_centers, start=1):
        for local_atom in template_atoms:
            atom_global_id += 1
            pos = center + local_atom
            # atom-ID  mol-ID  atom-type  charge  x  y  z
            f.write(f"{atom_global_id:7d}  {mol_id:5d}  1  0.0"
                    f"  {pos[0]:14.6f}  {pos[1]:14.6f}  {pos[2]:14.6f}\n")

print("Written: aa_c60_108.data")
