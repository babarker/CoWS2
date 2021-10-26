#!/usr/bin/env python

import numpy as np
import os
import matplotlib.pyplot as plt

def read_energies(dirlist):

    # This function requires as input a list of strings,
    # where each string is the name of the directories
    # that each contain a same-named output file.
    
    Etot = [] # Initialize list of total energies, to be read from output file
    
    for dd in dirlist:

        # FOR NOLAN:
        # edit the name of this output file to match what you called it.    
        fname = dd+'FILE.out' # edit FILE.out so that it is your file name
        ff = open(fname,'r')
        ln = ff.readlines()
        ff.close()
        
        for ll in ln:
            if '!' in ll:
                Etot.append(float(ll.split()[4]))
    return Etot

def read_zCo(dirlist):

    # This function requires as input a list of strings,
    # where each string is the name of the directories
    # that each contain a same-named INPUT file.
    
    zCo = [] # Initialize list of z-coordinates of Cobalt, to be read from INPUT files
    
    for dd in dirlist:

        # FOR NOLAN:
        # edit the name of this utput file to match what you called it.    
        fname = dd+'FILE.in' # edit FILE.in so that it is your file name
        ff = open(fname,'r')
        ln = ff.readlines()
        ff.close()
        
        for ii,ll in enumerate(ln):
            if 'ATOMIC_POSITIONS' in ll:
                for jj in range(ii+1,len[ln]):
                    if 'Co' in ln[jj]:
                        zCo.append(float(ln[jj].split()[3])
                        break
    return zCo

def quad_fit(zCo,Etot):

    # Given the Cobalt z-coordinate and the corresponding total energy,
    # compute the quadratic fit and the estimate for minimum position,
    # to be used as input for the relaxation calculation.
    
    # For the fit to be good, we need to know beforehand that we are in the
    # QUADRATIC region of energy, not the flat region of the Morse potential

    pfit = np.polyfit[zCo,Etot,2]
    # pfit[0] * z**2 + pfit[1] * z + pfit[2]
    
    # Estimated minimum from this fit occurs when first deriv. of above is zero:
    # 0 = 2 * pfit[0] * z_min + pfit[1]
    z_min = -0.5 pfit[1] / pfit[0]

    return(pfit,z_min)
    
def main():

    # FOR NOLAN:
    # edit the names of the directories (there may be something like six in total, as well)
    dirlist = [ DIRECTORY1, DIRECTORY2, DIRECTORY3 ]    
                
    Etot = read_energies(dirlist)
    zCo = read_zCo(dirlist)

    # Generally, keep this commented, until you know that you are only including
    # the parabolic part of the curve in the list of directories in dirlist
    #
    #pfit, z_min = quad_fit(zCo,Etot)

    
    # Make a plot
    plt.plot(zCo,Etot)
    plt.xlabel('Co atom z-coordinate (UNITS)')
    plt.xlabel('Total Energy (Ry)')
    
    plt.display()
    
    return
    
main()
