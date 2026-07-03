#!/bin/bash
#SBATCH -J cg_c60
#SBATCH -o %j_cg.out
#SBATCH -p regular
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -t 00:20:00

module load LAMMPS

# Generate the data file if it doesn't already exist
python3 gen_cg_data.py

srun lmp -in in.cg_fullerene > log_cg.out
