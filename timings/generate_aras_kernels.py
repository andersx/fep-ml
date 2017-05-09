#!/usr/bin/env python2

import sys

import os
import numpy as np
import fml
import time
import random
import ezpickle

from fml.kernels import get_atomic_kernels_aras

D_WIDTH = 0.2
CUT_DISTANCE = 4.0
R_WIDTH = 1.0 # 1.0
C_WIDTH = 1.0 # 0.5

def aras_kernels(mols1, mols2):

    sigmas = [0.1 * 2**i for i in range(20)]
    amax = mols1[0].aras_descriptor.shape[0]

    nm1 = len(mols1)
    nm2 = len(mols2)

    X1 = np.array([mol.aras_descriptor for mol in mols1]).reshape((nm1,amax,3+amax,amax))
    X2 = np.array([mol.aras_descriptor for mol in mols2]).reshape((nm2,amax,3+amax,amax))

    Z1 = [mol.nuclear_charges for mol in mols1]
    Z2 = [mol.nuclear_charges for mol in mols2]

    K = get_atomic_kernels_aras(X1, X2, Z1, Z2, sigmas, \
    t_width=np.pi/2.0, d_width=D_WIDTH, cut_distance=CUT_DISTANCE, r_width=R_WIDTH, c_width=R_WIDTH,
    order=1, scale_angular=1.0/10.0)

    return K

if __name__ == "__main__":
    
    path = "/home/andersx/projects/fep-ml/1-2/000/prot/V0/"
    filenames = os.listdir(path)
    filenames.sort()
    random.seed(666)
    random.shuffle(filenames)

    np.set_printoptions(linewidth=99999999999999999)
    print "Generating ARAD descriptors from FML interface ..."

    mols = []

    n = int(sys.argv[1])

    for filename in filenames[:n]:

        if ".xyz" not in filename:
            continue

        mol = fml.Molecule()
        mol.read_xyz(path + filename)
        mol.generate_aras_descriptor(size=218)
        mols.append(mol)

    print "ARAS Kernels"
    start = time.time()
    K = aras_kernels(mols, mols)
    print "Time:", time.time() - start
    np.save("K_aras.npy", K)
    print K.shape
