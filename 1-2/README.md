# The 1-2 ligand transformation

Herein are (a subset of) the structures needed to compute an MM -> QM correction to the free energy perturbation of ligand 1-> 2 in the paper by Olsson et al ([DOI: 10.1002/jcc.24375](http://onlinelibrary.wiley.com/doi/10.1002/jcc.24375/abstract))

The current folder contains two subfolders named `000` and `100` correspondning to the lambda values of 0.00 and 1.00, respectively.
The ligand MeBz (V0 or 2) is extracted at lambda = 0.00 and the ligand Bz (V1 or 1) is extracted at lambda = 1.00.

The structures contained herein are the complexes (starting with a `c`), the hosts (starting with an `r`) and the ligands (starting with an `l`).
All files included the geometries (stored in `.xyz` format) with the heat of formation energy obtained at the PM6-DH+ level of theory included in the title line.

**NB**: Please note that the hosts are *only* included in the lambda = 0.00 results.
