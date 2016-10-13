#!/usr/bin/python

# Operating system commands
import os
from os import path
import exceptions
import sys
import time
import atexit

import math
import numpy as np
import numpy.random as rnd
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.colors as colors
from mpl_toolkits.axes_grid import make_axes_locatable

import pylab
import vtk
from vtk.util.numpy_support import vtk_to_numpy

import re
import string

def x(model_name):
    """
    Read model name and return the corresponding
    array of x-coordinates of cell centers.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([0.5,1.5,2.5,3.5,            #1.0
                  4.25,4.75,5.25,5.75,    #0.5
                  6.1,6.3,6.5,6.7,6.9,    #0.2
                  7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95, #0.1
                  8.005,  8.015,  8.025,  8.035,  8.045,  8.055,  8.065,  8.075,
                  8.085,  8.095,  8.105,  8.115,  8.125,  8.135,  8.145,  8.155,
                  8.165,  8.175,  8.185,  8.195,  8.205,  8.215,  8.225,  8.235,
                  8.245,  8.255,  8.265,  8.275,  8.285,  8.295,  8.305,  8.315,
                  8.325,  8.335,  8.345,  8.355,  8.365,  8.375,  8.385,  8.395,
                  8.405,  8.415,  8.425,  8.435,  8.445,  8.455,  8.465,  8.475,
                  8.485,  8.495,  8.505,     # 0.01
                  8.5116,  8.5148,  8.518 ,  8.5212,  8.5244,  8.5276,  8.5308,
                  8.534 ,  8.5372,  8.5404,  8.5436,  8.5468,  8.55  ,  8.5532,
                  8.5564,  8.5596,  8.5628,  8.566 ,  8.5692,  8.5724,  8.5756,
                  8.5788,  8.582 ,  8.5852,  8.5884,  8.5916,  8.5948,  8.598 ,
                  8.6012,  8.6044,  8.6076,  8.6108,  8.614 ,  8.6172,  8.6204,
                  8.6236,  8.6268,  8.63  ,  8.6332,  8.6364,  8.6396,  8.6428,
                  8.646 ,  8.6492,  8.6524,  8.6556,  8.6588,  8.662 ,  8.6652,
                  8.6684,  8.6716,  8.6748,  8.678 ,  8.6812,  8.6844,  8.6876,
                  8.6908,  8.694 ,  8.6972,  8.7004,  8.7036,  8.7068,  8.71  ,
                  8.7132,  8.7164,  8.7196,  8.7228,  8.726 ,  8.7292,  8.7324,
                  8.7356,  8.7388,  8.742 ,  8.7452,  8.7484,  8.7516,  8.7548,
                  8.758 ,  8.7612,  8.7644,  8.7676,  8.7708,  8.774 ,  8.7772,
                  8.7804,  8.7836,  8.7868,  8.79  ,  8.7932,  8.7964,  8.7996,
                  8.8028,  8.806 ,  8.8092,  8.8124,  8.8156,  8.8188,  8.822 ,
                  8.8252,  8.8284,        #0.0032
                  8.835,  8.845,  8.855,  8.865,  8.875,  8.885,  8.895,  8.905,
                  8.915,  8.925,  8.935,  8.945,  8.955,  8.965,  8.975,  8.985,
                  8.995,  9.005,  9.015,  9.025,  9.035,  9.045,  9.055,  9.065,
                  9.075,  9.085,  9.095,  9.105,  9.115,  9.125,  9.135,  9.145,
                  9.155,  9.165,  9.175,  9.185,  9.195,  9.205,  9.215,  9.225,
                  9.235,  9.245,  9.255,  9.265,  9.275,  9.285,  9.295,  9.305,
                  9.315,  9.325,          #0.01
                  9.38,9.48,9.58,9.68,9.78,9.88,9.98,10.08,10.18,10.28, #0.1
                  10.43,10.63,10.83,11.03,11.23,   #0.2
                  11.58,12.08,12.58,13.08,         #0.5
                  13.83,14.83,15.83,16.83])        #1.0

    elif model_name == 'prescribedhead':
        arr = np.array([0.5+i*1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 
    return arr


def y(model_name):
    """
    Read model name and return the corresponding
    array of y-coordinates of cell centers.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([0.5,1.5,2.5,3.5,
                  4.25,4.75,5.25,5.75,
                  6.1,6.3,6.5,6.7,6.9,
                  7.05,7.15,7.25,7.35,7.45,7.55,7.65,7.75,7.85,7.95,
                  8.005,  8.015,  8.025,  8.035,  8.045,  8.055,  8.065,  8.075,
                  8.085,  8.095,  8.105,  8.115,  8.125,  8.135,  8.145,  8.155,
                  8.165,  8.175,  8.185,  8.195,  8.205,  8.215,  8.225,  8.235,
                  8.245,  8.255,  8.265,  8.275,  8.285,  8.295,  8.305,  8.315,
                  8.325,  8.335,  8.345,  8.355,  8.365,  8.375,  8.385,  8.395,
                  8.405,  8.415,  8.425,  8.435,  8.445,  8.455,  8.465,  8.475,
                  8.485,  8.495,  8.505,     # 0.01
                  8.5116,  8.5148,  8.518 ,  8.5212,  8.5244,  8.5276,  8.5308,
                  8.534 ,  8.5372,  8.5404,  8.5436,  8.5468,  8.55  ,  8.5532,
                  8.5564,  8.5596,  8.5628,  8.566 ,  8.5692,  8.5724,  8.5756,
                  8.5788,  8.582 ,  8.5852,  8.5884,  8.5916,  8.5948,  8.598 ,
                  8.6012,  8.6044,  8.6076,  8.6108,  8.614 ,  8.6172,  8.6204,
                  8.6236,  8.6268,  8.63  ,  8.6332,  8.6364,  8.6396,  8.6428,
                  8.646 ,  8.6492,  8.6524,  8.6556,  8.6588,  8.662 ,  8.6652,
                  8.6684,  8.6716,  8.6748,  8.678 ,  8.6812,  8.6844,  8.6876,
                  8.6908,  8.694 ,  8.6972,  8.7004,  8.7036,  8.7068,  8.71  ,
                  8.7132,  8.7164,  8.7196,  8.7228,  8.726 ,  8.7292,  8.7324,
                  8.7356,  8.7388,  8.742 ,  8.7452,  8.7484,  8.7516,  8.7548,
                  8.758 ,  8.7612,  8.7644,  8.7676,  8.7708,  8.774 ,  8.7772,
                  8.7804,  8.7836,  8.7868,  8.79  ,  8.7932,  8.7964,  8.7996,
                  8.8028,  8.806 ,  8.8092,  8.8124,  8.8156,  8.8188,  8.822 ,
                  8.8252,  8.8284,        #0.0032
                  8.835,  8.845,  8.855,  8.865,  8.875,  8.885,  8.895,  8.905,
                  8.915,  8.925,  8.935,  8.945,  8.955,  8.965,  8.975,  8.985,
                  8.995,  9.005,  9.015,  9.025,  9.035,  9.045,  9.055,  9.065,
                  9.075,  9.085,  9.095,  9.105,  9.115,  9.125,  9.135,  9.145,
                  9.155,  9.165,  9.175,  9.185,  9.195,  9.205,  9.215,  9.225,
                  9.235,  9.245,  9.255,  9.265,  9.275,  9.285,  9.295,  9.305,
                  9.315,  9.325,          #0.01
                  9.38,9.48,9.58,9.68,9.78,9.88,9.98,10.08,10.18,10.28,
                  10.43,10.63,10.83,11.03,11.23,
                  11.58,12.08,12.58,13.08,
                  13.83,14.83,15.83,16.83])
    elif model_name == 'prescribedhead':
        arr = np.array([0.5+i*1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 
    return arr

def xticks(model_name):
    """
    Read model name and return the corresponding
    array of x-coordinates of left side of cells.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([0.0,1.0,2.0,3.0,4.0,        
                  4.5,5.0,5.5,6.0,   
                  6.2,6.4,6.6,6.8,7.0,   
                  7.1,  7.2,  7.3,  7.4,  7.5,  7.6,  7.7,  7.8,  7.9,  8.0,
                  8.01,  8.02,  8.03,  8.04,  8.05,  8.06,  8.07,  8.08,  8.09,
                  8.1 ,  8.11,  8.12,  8.13,  8.14,  8.15,  8.16,  8.17,  8.18,
                  8.19,  8.2 ,  8.21,  8.22,  8.23,  8.24,  8.25,  8.26,  8.27,
                  8.28,  8.29,  8.3 ,  8.31,  8.32,  8.33,  8.34,  8.35,  8.36,
                  8.37,  8.38,  8.39,  8.4 ,  8.41,  8.42,  8.43,  8.44,  8.45,
                  8.46,  8.47,  8.48,  8.49,  8.5 ,  8.51,
                  8.5132,  8.5164,  8.5196,  8.5228,  8.526 ,  8.5292,  8.5324,
                  8.5356,  8.5388,  8.542 ,  8.5452,  8.5484,  8.5516,  8.5548,
                  8.558 ,  8.5612,  8.5644,  8.5676,  8.5708,  8.574 ,  8.5772,
                  8.5804,  8.5836,  8.5868,  8.59  ,  8.5932,  8.5964,  8.5996,
                  8.6028,  8.606 ,  8.6092,  8.6124,  8.6156,  8.6188,  8.622 ,
                  8.6252,  8.6284,  8.6316,  8.6348,  8.638 ,  8.6412,  8.6444,
                  8.6476,  8.6508,  8.654 ,  8.6572,  8.6604,  8.6636,  8.6668,
                  8.67  ,  8.6732,  8.6764,  8.6796,  8.6828,  8.686 ,  8.6892,
                  8.6924,  8.6956,  8.6988,  8.702 ,  8.7052,  8.7084,  8.7116,
                  8.7148,  8.718 ,  8.7212,  8.7244,  8.7276,  8.7308,  8.734 ,
                  8.7372,  8.7404,  8.7436,  8.7468,  8.75  ,  8.7532,  8.7564,
                  8.7596,  8.7628,  8.766 ,  8.7692,  8.7724,  8.7756,  8.7788,
                  8.782 ,  8.7852,  8.7884,  8.7916,  8.7948,  8.798 ,  8.8012,
                  8.8044,  8.8076,  8.8108,  8.814 ,  8.8172,  8.8204,  8.8236,
                  8.8268,  8.83,
                  8.84,  8.85,  8.86,  8.87,  8.88,  8.89,  8.9 ,  8.91,  8.92,
                  8.93,  8.94,  8.95,  8.96,  8.97,  8.98,  8.99,  9.  ,  9.01,
                  9.02,  9.03,  9.04,  9.05,  9.06,  9.07,  9.08,  9.09,  9.1 ,
                  9.11,  9.12,  9.13,  9.14,  9.15,  9.16,  9.17,  9.18,  9.19,
                  9.2 ,  9.21,  9.22,  9.23,  9.24,  9.25,  9.26,  9.27,  9.28,
                  9.29,  9.3 ,  9.31,  9.32,  9.33,
                  9.43,   9.53,   9.63,   9.73,   9.83,   9.93,  10.03,  10.13,
                  10.23,  10.33,
                  10.53,10.73,10.93,11.13, 11.33,
                  11.83,12.33,12.83,13.33,       
                  14.33,15.33,16.33,17.33])      
    elif model_name == 'prescribedhead':
        arr = np.array([0.0+i*1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name)
    return arr

def yticks(model_name):
    """
    Read model name and return the corresponding
    array of y-coordinates of front side of cells.
    """

    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([0.0,1.0,2.0,3.0,4.0,        
                  4.5,5.0,5.5,6.0,   
                  6.2,6.4,6.6,6.8,7.0,   
                  7.1,  7.2,  7.3,  7.4,  7.5,  7.6,  7.7,  7.8,  7.9,  8.0,
                  8.01,  8.02,  8.03,  8.04,  8.05,  8.06,  8.07,  8.08,  8.09,
                  8.1 ,  8.11,  8.12,  8.13,  8.14,  8.15,  8.16,  8.17,  8.18,
                  8.19,  8.2 ,  8.21,  8.22,  8.23,  8.24,  8.25,  8.26,  8.27,
                  8.28,  8.29,  8.3 ,  8.31,  8.32,  8.33,  8.34,  8.35,  8.36,
                  8.37,  8.38,  8.39,  8.4 ,  8.41,  8.42,  8.43,  8.44,  8.45,
                  8.46,  8.47,  8.48,  8.49,  8.5 ,  8.51,
                  8.5132,  8.5164,  8.5196,  8.5228,  8.526 ,  8.5292,  8.5324,
                  8.5356,  8.5388,  8.542 ,  8.5452,  8.5484,  8.5516,  8.5548,
                  8.558 ,  8.5612,  8.5644,  8.5676,  8.5708,  8.574 ,  8.5772,
                  8.5804,  8.5836,  8.5868,  8.59  ,  8.5932,  8.5964,  8.5996,
                  8.6028,  8.606 ,  8.6092,  8.6124,  8.6156,  8.6188,  8.622 ,
                  8.6252,  8.6284,  8.6316,  8.6348,  8.638 ,  8.6412,  8.6444,
                  8.6476,  8.6508,  8.654 ,  8.6572,  8.6604,  8.6636,  8.6668,
                  8.67  ,  8.6732,  8.6764,  8.6796,  8.6828,  8.686 ,  8.6892,
                  8.6924,  8.6956,  8.6988,  8.702 ,  8.7052,  8.7084,  8.7116,
                  8.7148,  8.718 ,  8.7212,  8.7244,  8.7276,  8.7308,  8.734 ,
                  8.7372,  8.7404,  8.7436,  8.7468,  8.75  ,  8.7532,  8.7564,
                  8.7596,  8.7628,  8.766 ,  8.7692,  8.7724,  8.7756,  8.7788,
                  8.782 ,  8.7852,  8.7884,  8.7916,  8.7948,  8.798 ,  8.8012,
                  8.8044,  8.8076,  8.8108,  8.814 ,  8.8172,  8.8204,  8.8236,
                  8.8268,  8.83,
                  8.84,  8.85,  8.86,  8.87,  8.88,  8.89,  8.9 ,  8.91,  8.92,
                  8.93,  8.94,  8.95,  8.96,  8.97,  8.98,  8.99,  9.  ,  9.01,
                  9.02,  9.03,  9.04,  9.05,  9.06,  9.07,  9.08,  9.09,  9.1 ,
                  9.11,  9.12,  9.13,  9.14,  9.15,  9.16,  9.17,  9.18,  9.19,
                  9.2 ,  9.21,  9.22,  9.23,  9.24,  9.25,  9.26,  9.27,  9.28,
                  9.29,  9.3 ,  9.31,  9.32,  9.33,
                  9.43,   9.53,   9.63,   9.73,   9.83,   9.93,  10.03,  10.13,
                  10.23,  10.33,
                  10.53,10.73,10.93,11.13, 11.33,
                  11.83,12.33,12.83,13.33,       
                  14.33,15.33,16.33,17.33])      
    elif model_name == 'prescribedhead':
        arr = np.array([0.0+i*1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name)
    return arr

def delx(model_name):
    """
    Read model name and return the corresponding
    array of cell lengths in x-direction.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([1.0,1.0,1.0,1.0,
                     0.5,0.5,0.5,0.5,
                     0.2,0.2,0.2,0.2,0.2,
                     0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
                     0.2,0.2,0.2,0.2,0.2,
                     0.5,0.5,0.5,0.5,
                     1.0,1.0,1.0,1.0])             # [m]

    elif model_name == 'prescribedhead':
        arr = np.array([1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 
    return arr

def dely(model_name):
    """
    Read model name and return the corresponding
    array of cell lengths in y-direction.
    """
    if model_name == 'headbctest' or model_name == 'alexdiff':
        arr = np.array([1.0,1.0,1.0,1.0,
                     0.5,0.5,0.5,0.5,
                     0.2,0.2,0.2,0.2,0.2,
                     0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,0.0032,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
                     0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,
                     0.2,0.2,0.2,0.2,0.2,
                     0.5,0.5,0.5,0.5,
                     1.0,1.0,1.0,1.0])             # [m]

    elif model_name == 'prescribedhead':
        arr = np.array([1.0 for i in range(31)])
    else:
        raise exceptions.RuntimeError('Model name not valid: '+model_name) 
    return arr
