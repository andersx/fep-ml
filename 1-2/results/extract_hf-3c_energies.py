from __future__ import print_function

import csv
import os
import sys

import numpy


def read_xyz_energy(filename):
    with open(filename, 'r') as fhf:
        for line2 in fhf:
            if "FINAL SINGLE POINT" in line2:
                tokens2 = line2.split()
                energy = float(tokens2[-1])*627.51
                return energy

    raise EOFError("Could not properly read the file '{}'".format(filename))


def iter_files(system, index):
    """ iterator for files in project """
    #for i in range(2000, 2500):
    for i in range(1, 4001):

        p = "../{0:d}00/{1:s}/V{0:d}".format(index, system)
        pp = "../000/{0:s}/V0".format(system)
        cplx = os.path.join(p, "c{0:d}_hf.out".format(i))
        recp = os.path.join(pp, "r{0:d}_hf.out".format(i))
        lig = os.path.join(p, "l{0:d}_hf.out".format(i))
        yield i, cplx, recp, lig


def iter_energies(system, index):
    for i, c, r, l in iter_files(system, index):
        c_erg = read_xyz_energy(c)
        r_erg = read_xyz_energy(r)
        l_erg = read_xyz_energy(l)
        try:
            de = c_erg - r_erg - l_erg
        except TypeError:
            print("FAILED FAILED\n{}\nFAILED".format(i))
            raise TypeError("LOL")
        else:
            yield i, c_erg, r_erg, l_erg, de


if __name__ == '__main__':
    data = []
    for system in ['prot', 'wat']:
        for index in [1]: #[0, 1]
            filename = "{1:d}00_{0:s}_hf-3c_energies.csv".format(system, index)
            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                try:
                    for i, c, r, l, de in iter_energies(system, index):
                        writer.writerow([i, c, r, l, de])
                except TypeError:
                    print("{0:d}_{1:s} failed with TypeError.".format(index, system))
                except EOFError:
                    print("{0:d}_{1:s} failed with EOFError. Index = {2:d}".format(index, system, i))
