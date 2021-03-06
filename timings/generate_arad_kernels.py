#!/usr/bin/env python2

import sys

import os
import numpy as np
import fml
import time
import random

D_WIDTH = 0.2
CUT_DISTANCE = 4.0
R_WIDTH = 1.0 # 1.0
C_WIDTH = 1.0 # 0.5

def arad_kernels(mols1, mols2):

    from fml.kernels import get_atomic_kernels_arad

    sigmas = [0.1 * 2**i for i in range(20)]
    # sigmas = [25.0]

    amax = 218

    nm1 = len(mols1)
    nm2 = len(mols2)

    X1 = np.array([mol.arad_descriptor for mol in mols1]).reshape((nm1,amax,5,amax))
    X2 = np.array([mol.arad_descriptor for mol in mols2]).reshape((nm2,amax,5,amax))

    Z1 = [mol.nuclear_charges for mol in mols1]
    Z2 = [mol.nuclear_charges for mol in mols2]

    K = get_atomic_kernels_arad(X1, X2, Z1, Z2, sigmas, \
        width=D_WIDTH, cut_distance=CUT_DISTANCE, r_width=R_WIDTH, c_width=C_WIDTH)

    return K

if __name__ == "__main__":
    
    path = "/home/andersx/projects/fep-ml/1-2/000/prot/V0/"
    filenames = os.listdir(path)
    filenames.sort()
    random.seed(666)
    random.shuffle(filenames)

    np.set_printoptions(linewidth=99999999999999999)
    print "Generating ARAS descriptors from FML interface ..."

    n = int(sys.argv[1])

    mols = []
    for filename in filenames[:n]:

        if ".xyz" not in filename:
            continue

        mol = fml.Molecule()
        mol.read_xyz(path + filename)
        mol.generate_arad_descriptor(size=218)
        mols.append(mol)

    print "ARAD Kernels"
    start = time.time()
    K = arad_kernels(mols, mols)
    print "Time:", time.time() - start
    np.save("K_arad.npy", K)

    print K.shape
