import os
from time import time
import random
import sys

import numpy

import fml
import fml.kernels
import fml.math


def load(filenames):
    data = []
    for file in filenames:
        if not 'xyz' in file:
            continue
        m = fml.Molecule()
        m.read_xyz(file)
        m.generate_coulomb_matrix(size=218)
        data.append(m)

    return data

def predict(train_size, test_size):
    sigma = 820.0
    files = sorted(os.listdir('.'))

    random.seed(666) # the gates are open!
    random.shuffle(files)
    training_files = files[:train_size]
    test_files = files[train_size:train_size+test_size]
    
    # load both training
    training_mols = load(training_files)
    test_mols = load(test_files)
    
    # learning komputah
    # three steps:
    # 1) coulomb matrices
    # 2) kernel
    # 3) not profit yet
    training_CMs = numpy.array([m.coulomb_matrix for m in training_mols]).T
    K = fml.kernels.gaussian_kernel(training_CMs, training_CMs, sigma)
    rhs = numpy.array([m.energy for m in training_mols])
    alpha = fml.math.cho_solve(K, rhs)
    
    # use komputah
    # 
    test_CMs = numpy.array([m.coulomb_matrix for m in test_mols]).T
    Ks = fml.kernels.gaussian_kernel(training_CMs, test_CMs, sigma).T
    test_rhs = numpy.array([m.energy for m in test_mols])
    
    pred = Ks.dot(alpha)
    
    return numpy.mean(numpy.abs(pred - test_rhs))

train_sizes = [100, 200, 400, 800]
for t in train_sizes:
    start = time()
    mae = predict(t, 400)
    end = time() - start
    print "%6d %9.4f T=%6.2f" % (t, mae, end)
