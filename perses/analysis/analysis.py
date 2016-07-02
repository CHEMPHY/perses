"""
Analysis tools for perses automated molecular design.

TODO
----

"""

__author__ = 'John D. Chodera'

################################################################################
# IMPORTS
################################################################################

import os, os.path
import sys, math
import numpy as np
import copy
import time
import netCDF4 as netcdf
import cPickle as pickle

import matplotlib
import seaborn

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

################################################################################
# LOGGER
################################################################################

import logging
logger = logging.getLogger(__name__)

################################################################################
# ANALYSIS
################################################################################

class Analysis(object):
    """Analysis tools for perses automated design.

    """
    def __init__(self, storage_filename):
        """Open a storage file for analysis.

        """
        # TODO: Replace this with calls to storage API
        self._ncfile = netcdf.Dataset(storage_filename, 'r')

    def get_environments(self):
        """Return a list of environments in storage file.

        Returns
        -------
        environments : list of str
           List of environment names in storage (e.g. []'explicit-complex', 'explicit-ligand'])

        """
        environments = list()
        for group in self._ncfile.groups:
            environments.append( str(group) )
        return environments

    def plot_ncmc_work(self, filename):
        """Generate plots of NCMC work.

        Parameters
        ----------
        filename : str
            File to write PDF of NCMC work plots to.

        """
        with PdfPages(filename) as pdf:
            for envname in self.get_environments():
                modname = 'NCMCEngine'
                work = dict()
                for direction in ['delete', 'insert']:
                    varname = '/' + envname + '/' + modname + '/' + 'work_' + direction
                    try:
                        work[direction] = self._ncfile[varname][:,:]
                        print('Found %s' % varname)
                    except Exception as e:
                        pass

                if len(work) > 0:
                    plt.figure(figsize=(6, 6))

                    for (index, direction) in enumerate(['delete', 'insert']):
                        plt.subplot(2,1,index+1)
                        plt.plot(work[direction].T, 'k-')
                        if index == 2: plt.xlabel('steps')
                        plt.ylabel('work / kT')
                        plt.title(direction)

                    pdf.savefig()  # saves the current figure into a pdf page
                    plt.close()
