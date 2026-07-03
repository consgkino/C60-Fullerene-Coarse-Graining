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
