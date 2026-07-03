# C60 Fullerene Coarse-Graining

This repository contains the input files, Python scripts, and analysis results for a coarse-graining study of C60 fullerene molecules.

The all-atom reference simulations are used to obtain structural information and interaction behavior between C60 molecules. The simulation was run using LAMMPS. The coarse-grained model is then tested by comparing its radial distribution function against the all-atom reference. Lennard-Jones potential, atomistic models and iterative Boltzmann models are compared


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
```

## Results

### Radial Distribution Function Comparison

The figure below compares the radial distribution function, \(g(r)\), between the all-atom C60 reference simulation and the coarse-grained C60 model.

![RDF comparison](figures/rdf_comparison_v2%20copy.png)

The RDF shows the probability of finding another C60 molecule at a distance \(r\) from a reference molecule. At large distances, both curves should approach \(g(r)=1\), which corresponds to bulk-like behavior.

The comparison shows that the coarse-grained model captures the general structural behavior of the all-atom reference. However, differences in the first peak position and peak height indicate that the Lennard-Jones coarse-grained model does not perfectly reproduce the atomistic structure.

## Conclusion

This project demonstrates the workflow for constructing and testing a coarse-grained model of C60 fullerene molecules. The all-atom model provides the reference behavior, while the coarse-grained model provides a simplified and computationally cheaper representation.

The RDF comparison shows that the coarse-grained model can reproduce the general structural behavior of the all-atom system, but quantitative differences remain due to the simplification of representing each C60 molecule as a single bead.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
