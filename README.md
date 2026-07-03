# C60 Fullerene Coarse-Graining

This repository contains the input files, Python scripts, and analysis results for a coarse-graining study of C60 fullerene molecules. The aim of the project is to compare an all-atom C60 model with a coarse-grained model where each C60 molecule is represented as a single bead.

The all-atom reference simulations are used to obtain structural information and interaction behavior between C60 molecules. The coarse-grained model is then tested by comparing its radial distribution function against the all-atom reference.

---

## Project Aim

The main goal of this project is to investigate how well a simplified coarse-grained C60 model can reproduce the structure of an all-atom fullerene system.

In the all-atom model, each C60 molecule contains 60 carbon atoms and the interactions are described using an atomistic force field. In the coarse-grained model, each C60 molecule is replaced by one effective particle interacting through a Lennard-Jones potential.

This reduces the number of particles significantly and allows simulations to be performed more efficiently. However, the simplification also introduces quantitative errors, so the coarse-grained results must be compared carefully with the all-atom reference.

---

## Repository Structure

```text
C60-Fullerene-Coarse-Graining/
├── gen_aa_multi_data.py          # Python script to generate the all-atom C60 data file
├── in.aa_multi_fullerene         # LAMMPS input file for the all-atom simulation
├── run_aa_multi.sh               # Shell script used to run the all-atom simulation
├── aa_multi_run/                 # Folder for all-atom simulation outputs
├── cg_run/                       # Folder for coarse-grained simulation outputs
├── figures/                      # Folder containing result plots
└── README.md


## Results

### Radial Distribution Function Comparison

The figure below compares the radial distribution function, \(g(r)\), of the all-atom C60 system and the coarse-grained C60 model.

![RDF comparison](figures/rdf_comparison_v2%20copy.png)

The RDF shows the probability of finding another C60 molecule at a distance \(r\) from a reference C60 molecule. At large distances, both curves should approach \(g(r)=1\), which corresponds to bulk-like behavior.

The comparison shows that the coarse-grained model captures the overall structural behavior of the all-atom reference. However, differences in the first peak position and height indicate that the coarse-grained Lennard-Jones model does not reproduce the atomistic structure perfectly. This is expected because each C60 molecule is simplified into one spherical bead.

---

### Interpretation of the RDF

The first RDF peak corresponds to the most probable nearest-neighbor distance between C60 molecules. If the coarse-grained model were perfect, the first peak of the CG RDF would overlap with the all-atom RDF peak.

Any shift in the first peak means that the effective bead-bead interaction does not produce exactly the same equilibrium spacing as the all-atom model. A difference in peak height means that the local ordering or packing strength is different between the two models.

Therefore, the RDF comparison is useful for judging whether the coarse-grained potential gives a realistic structural description of the fullerene system.

---

### Main Result

The coarse-grained model reproduces the qualitative behavior of the all-atom system, especially the long-distance RDF behavior. However, quantitative differences remain near the first-neighbor region. This shows the limitation of representing a full C60 molecule as a single Lennard-Jones bead.
