from __future__ import print_function

import csv
import os
import sys

import numpy


def read_xyz_energy(filename):
    """ Reads the energy of the provided .xyz file """
    energy = 0.0
    with open(filename, 'r') as f:
        n_lines = int(f.readline())
        energy = float(f.readline())

    return energy


def iter_files(system, index):
    """ iterator for files in project """
    for i in range(1, 4001):

        p = "../{0:d}00/{1:s}".format(index, system)
        pp = "../000/{0:s}".format(system)
        cplx = os.path.join(p, "c{0:d}.xyz".format(i))
        recp = os.path.join(pp, "r{0:d}.xyz".format(i))
        lig = os.path.join(p, "l{0:d}.xyz".format(i))
        yield i, cplx, recp, lig


def iter_energies(system, index):
    for i, c, r, l in iter_files(system, index):
        c_erg = read_xyz_energy(c)
        r_erg = read_xyz_energy(r)
        l_erg = read_xyz_energy(l)
        yield i, c_erg, r_erg, l_erg, c_erg - r_erg - l_erg


if __name__ == '__main__':
    data = []
    for system in ['prot', 'wat']:
        for index in [0, 1]:
            filename = "{1:d}00_{0:s}_pm6_energies.csv".format(system, index)
            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                for i, c, r, l, de in iter_energies(system, index):
                    writer.writerow([i, c, r, l, de])
