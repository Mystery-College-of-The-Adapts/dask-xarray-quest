#!/usr/bin/env bash
qsub -I -l select=4:ncpus=1:mpiprocs=1 -l walltime=60:00 -q regular -A STDD0004
