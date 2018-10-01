# Folder containing computed quantities
The results are stored in plain `.csv` files in the following format:

    INDEX   E(COMPLEX)   E(RECEPTOR)   E(LIGAND)    dE

where `dE` is the binding energy computed from

    dE = E(COMPLEX) - E(RECEPTOR) - E(LIGAND)

All units stored are en kcal/mol.
Note that for PM6, the results are heats of formation whereas for HF-3c results the energies are converted directly from the Hartree energies
