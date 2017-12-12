# Read routine for errorplot arrays

import os
import numpy as np

from mypackage.plot import plotarrays as pa
from mypackage.run import pythonmodule as pm
from mypackage.errorplot import arrays as ea

import exceptions

def read(which_methods,
         n_runs = 1000,
         model = 'wavebc',
         which_res = 'endres',
         stat_method = 'mean',
):
    """
    Reads residual arrays at beginning (begres) or
    end (endres) of the EnKF run and calculates
    an array of given statistical measure.

    Parameters
    ----------
    which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays.

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    stat_method : string
        'mean' - Calculate means
        'std' - Standard deviation
        'stdm' - Standard deviation of the mean
        'median' - Median or 50 Percentile
        'q25' - 25 Percentile
        'q75' - 75 Percentile

    Returns
    -------
    stat_array : array
        Array containing the statistical measures.

    stat_array_name : string
        Containing proposed saving location for array.
    """

    # Input check
    if not which_res in ['endres','begres']:
        raise exceptions.RuntimeError("which_res has to be 'endres' or 'begres'")
    if not stat_method in ['mean','std','stdm','median','q25','q75']:
        raise exceptions.RuntimeError('stat_method wrong')
    if not n_runs in [100,1000]:
        raise exceptions.RuntimeError('n_runs wrong')
    if not model in ['wavebc','wave','wavewell']:
        raise exceptions.RuntimeError('model wrong')

    # Nunber of methods
    num_methods = len(which_methods)

    # Ensemble sizes
    ensemble_sizes = ([50,70,100,250] if n_runs==1000 else [500,1000,2000])

    # Initialize stat_array
    stat_array = np.zeros([num_methods,len(ensemble_sizes)])

    # i_kind: counter
    # j_kind: method-index
    for i_kind, j_kind in enumerate(which_methods):
        for j, enssize in enumerate(ensemble_sizes):

            # Get date and time
            dat = pa.dats[model][n_runs][j_kind][enssize]
            let = pa.lets[model][n_runs][j_kind][enssize]
            num = pa.nums[model][n_runs][j_kind][enssize]

            # Read residuals
            res = np.load(pm.py_output_filename('dists',which_res,model+'_'+dat+'_'+let,'npy'))

            # Calculate statistical quantitiy
            if stat_method == 'mean':
                stat_array[i_kind,j] = np.mean(res)
            elif stat_method == 'std':
                stat_array[i_kind,j] = np.std(res)
            elif stat_method == 'stdm':
                stat_array[i_kind,j] = np.std(res)/np.sqrt(num)
            elif stat_method == 'median':
                stat_array[i_kind,j] = np.percentile(res,50)
            elif stat_method == 'q25':
                stat_array[i_kind,j] = np.percentile(res,25)
            elif stat_method == 'q75':
                stat_array[i_kind,j] = np.percentile(res,75)


    # Name of the array
    stat_array_name = pm.py_output_filename(ea.tag,which_res,stat_method+'_'+str(n_runs)+'_'+model+'_'+'_'.join([str(i) for i in which_methods]),'npy')


    return stat_array, stat_array_name
