# Folder containing computed quantities
The results are stored in plain `.csv` files in the following format:

    INDEX   E(COMPLEX)   E(RECEPTOR)   E(LIGAND)    dE

where `dE` is the binding energy computed from

    dE = E(COMPLEX) - E(RECEPTOR) - E(LIGAND)
