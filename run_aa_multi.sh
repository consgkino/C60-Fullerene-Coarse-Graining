#!/bin/bash
#SBATCH -J aa_c60_108
#SBATCH -o %j_aa.out
#SBATCH -p regular
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -t 03:00:00

module load LAMMPS

# Generate the data file if it doesn't already exist
python3 gen_aa_multi_data.py

srun lmp -in in.aa_multi_fullerene > log_aa.out
