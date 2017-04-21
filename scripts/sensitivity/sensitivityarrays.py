#!/usr/bin/python

###############################################################################
#                      Variables for Sensitivity Analysis                     #
###############################################################################

import numpy as np

tag = "sensitivity"

# Different runs ##############################################################
runs = [['cubey','2017_01_15',range(1000)],
        ['cubey','2017_01_31',range(1000)],
        ['cubey','2017_01_31',range(1001,2001)],
        # ['cubey','2017_01_31',range(2001,3001)],
        ['cubey','2017_01_30',range(1000)],
        ['cubey','2017_01_30',range(1001,2001)],
        ['cubey','2017_01_30',range(2001,3001)],
        # ['cubey','2017_01_30',range(3001,4001)],
]
        
varranges = {'cubey_2017_01_15_a':np.arange(0.5*10**6,3.5*10**6,0.003*10**6),
             'cubey_2017_01_31_a':np.arange(0.5*10**6,3.5*10**6,0.003*10**6),
             'cubey_2017_01_31_aln':np.arange(0.5*10**6,3.5*10**6,0.003*10**6),
             'cubey_2017_01_31_bxz':np.arange(0.5*10**6,3.5*10**6,0.003*10**6),
             'cubey_2017_01_30_a':np.arange(0.1,3.1,0.003),
             'cubey_2017_01_30_aln':np.arange(0.1,3.1,0.003),
             'cubey_2017_01_30_bxz':np.arange(0.1,3.1,0.003),
             'cubey_2017_01_30_dkl':np.arange(0.1,3.1,0.003),
             'cubey_2017_02_02_cx':np.arange(0.0,1.0*10**-7,0.1*10**-7),
             'cubey_2017_02_02_dh':np.arange(0.0,1.0*10**-6,0.1*10**-6),
             'cubey_2017_02_02_dr':np.arange(0.0,1.0*10**-5,0.1*10**-5),
             'cubey_2017_02_02_b':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_l':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_v':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_af':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_ap':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_az':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_bj':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_bt':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_02_cd':np.arange(0.1,3.1,0.3),
             'cubey_2017_02_08_b':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_l':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_v':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_af':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_ap':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_az':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_bj':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_bt':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
             'cubey_2017_02_08_cd':np.arange(0.5*10**6,3.5*10**6,0.3*10**6),
         }

varranges_sense = {'cubey_2017_01_15_a':np.array([1.22*10**6,1.49*10**6]),
                   'cubey_2017_01_31_a':np.array([1.22*10**6,1.49*10**6]),
                   'cubey_2017_01_31_aln':np.array([3.1*10**6,3.5*10**6]),
                   'cubey_2017_01_30_a':np.array([2.4,3.1]),
                   'cubey_2017_01_30_aln':np.array([2.4,3.1]),
                   'cubey_2017_01_30_bxz':np.array([1.0,2.5]),
}

senselets = []


# Sensitivity analysis: Varied variables ######################################
sensitivity_varnames = {'cubey_2016_12_13_a':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_a':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_aln':'Thermal conductivity deprecated',
                        'cubey_2016_12_14_bxz':'Thermal conductivity deprecated',
                        'cubey_2017_01_15_a':'Volumetric heat capacity',
                        'cubey_2017_01_16_a':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_16_aln':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_16_bxz':'Volumetric heat capacity deprecated',
                        'cubey_2017_01_31_a':'Volumetric heat capacity',
                        'cubey_2017_01_31_aln':'Volumetric heat capacity',
                        'cubey_2017_01_31_bxz':'Volumetric heat capacity',
                        'cubey_2017_01_30_a':'Thermal conductivity',
                        'cubey_2017_01_30_aln':'Thermal conductivity',
                        'cubey_2017_01_30_bxz':'Thermal conductivity',
                        'cubey_2017_01_30_dkl':'Thermal conductivity',
                        'cubey_2017_02_02_b':'Thermal conductivity v= 10**-7',
                        'cubey_2017_02_02_l':'Thermal conductivity v= 10**-7',
                        'cubey_2017_02_02_v':'Thermal conductivity v= 10**-7',
                        'cubey_2017_02_02_af':'Thermal conductivity v= 10**-6',
                        'cubey_2017_02_02_ap':'Thermal conductivity v= 10**-6',
                        'cubey_2017_02_02_az':'Thermal conductivity v= 10**-6',
                        'cubey_2017_02_02_bj':'Thermal conductivity v= 10**-5',
                        'cubey_2017_02_02_bt':'Thermal conductivity v= 10**-5',
                        'cubey_2017_02_02_cd':'Thermal conductivity v= 10**-5',
                        'cubey_2017_02_02_cx':'Velocity',
                        'cubey_2017_02_02_dh':'Velocity',
                        'cubey_2017_02_02_dr':'Velocity',
                        'cubey_2017_02_08_b':'Volumetric heat capacity v= 10**-7',
                        'cubey_2017_02_08_l':'Volumetric heat capacity v= 10**-7',
                        'cubey_2017_02_08_v':'Volumetric heat capacity v= 10**-7',
                        'cubey_2017_02_08_af':'Volumetric heat capacity v= 10**-6',
                        'cubey_2017_02_08_ap':'Volumetric heat capacity v= 10**-6',
                        'cubey_2017_02_08_az':'Volumetric heat capacity v= 10**-6',
                        'cubey_2017_02_08_bj':'Volumetric heat capacity v= 10**-5',
                        'cubey_2017_02_08_bt':'Volumetric heat capacity v= 10**-5',
                        'cubey_2017_02_08_cd':'Volumetric heat capacity v= 10**-5',
}

# Cubey: Unit numbers #########################################################
unit_numbers = {'cubey_2016_12_13_a': 1,
                'cubey_2016_12_14_a':2,
                'cubey_2016_12_14_aln':7,
                'cubey_2016_12_14_bxz':3,
                'cubey_2017_01_15_a':1,
                'cubey_2017_01_16_a':2,
                'cubey_2017_01_16_aln':7,
                'cubey_2017_01_16_bxz':3,
                'cubey_2017_01_31_a':2,
                'cubey_2017_01_31_aln':7,
                'cubey_2017_01_31_bxz':3,
                'cubey_2017_01_30_a':1,
                'cubey_2017_01_30_aln':2,
                'cubey_2017_01_30_bxz':7,
                'cubey_2017_01_30_dkl':3,
                'cubey_2017_02_02_b':1,
                'cubey_2017_02_02_l':2,
                'cubey_2017_02_02_v':7,
                'cubey_2017_02_02_af':1,
                'cubey_2017_02_02_ap':2,
                'cubey_2017_02_02_az':7,
                'cubey_2017_02_02_bj':1,
                'cubey_2017_02_02_bt':2,
                'cubey_2017_02_02_cd':7,
                'cubey_2017_02_02_cx':0,
                'cubey_2017_02_02_dh':0,
                'cubey_2017_02_02_dr':0,
                'cubey_2017_02_08_b':1,
                'cubey_2017_02_08_l':2,
                'cubey_2017_02_08_v':7,
                'cubey_2017_02_08_af':1,
                'cubey_2017_02_08_ap':2,
                'cubey_2017_02_08_az':7,
                'cubey_2017_02_08_bj':1,
                'cubey_2017_02_08_bt':2,
                'cubey_2017_02_08_cd':7,
}

# Cubey: Unit names ###########################################################
unit_names =  {0:'Velocity, bc',
               1:'Sand, outside',
               2:'Sand, inside',
               7:'Hull, large tube',
               3:'Inside, small tube',
}

# Sensitivity analysis: Strings of Ranges #####################################
sensitivity_ranges = {'cubey_2016_12_13_a':r'1.5-3.0 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_a':r'0.5-1.5 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_aln':r'1.0-3.0 $\frac{W}{mK}$ deprecated',
                      'cubey_2016_12_14_bxz':r'0.1-1.1 $\frac{W}{mK}$ deprecated',
                      'cubey_2017_01_15_a':r'1.22-1.49 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_16_a':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_16_aln':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_16_bxz':r'0.5-3.5 $\frac{J}{Km^3}$ deprecated',
                      'cubey_2017_01_31_a':r'1.22-1.49 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_31_aln':r'3.1-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_31_bxz':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_01_30_a':r'2.4-3.1 $\frac{W}{mK}$',
                      'cubey_2017_01_30_aln':r'2.4-3.1 $\frac{W}{mK}$',
                      'cubey_2017_01_30_bxz':r'1.0-2.5 $\frac{W}{mK}$',
                      'cubey_2017_01_30_dkl':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_b':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_l':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_v':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_af':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_ap':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_az':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_bj':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_bt':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_cd':r'0.1-3.1 $\frac{W}{mK}$',
                      'cubey_2017_02_02_cx':r'0.0-1.0 $10^{-7} \frac{m}{s}$',
                      'cubey_2017_02_02_dh':r'0.0-1.0 $10^{-6} \frac{m}{s}$',
                      'cubey_2017_02_02_dr':r'0.0-1.0 $10^{-5} \frac{m}{s}$',
                      'cubey_2017_02_08_b':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_l':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_v':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_af':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_ap':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_az':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_bj':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_bt':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
                      'cubey_2017_02_08_cd':r'0.5-3.5 $10^6 \frac{J}{Km^3}$',
}


# Sensitivity analysis: Default numbers #######################################
default_values = {'cubey_2017_01_15_a':1.36*10**6,
                  'cubey_2017_01_31_a':1.36*10**6,
                  'cubey_2017_01_31_aln':3.3*10**6,
                  'cubey_2017_01_31_bxz':1.0*10**6,
                  'cubey_2017_01_30_a':2.7,
                  'cubey_2017_01_30_aln':2.7,
                  'cubey_2017_01_30_bxz':2.0,
                  'cubey_2017_01_30_dkl':0.325,
                  'cubey_2017_02_02_b':2.6,
                  'cubey_2017_02_02_l':1.0,
                  'cubey_2017_02_02_v':2.0,
                  'cubey_2017_02_02_af':2.6,
                  'cubey_2017_02_02_ap':1.0,
                  'cubey_2017_02_02_az':2.0,
                  'cubey_2017_02_02_bj':2.6,
                  'cubey_2017_02_02_bt':1.0,
                  'cubey_2017_02_02_cd':2.0,
                  'cubey_2017_02_02_cx':0.0,
                  'cubey_2017_02_02_dh':0.0,
                  'cubey_2017_02_02_dr':0.0,
                  'cubey_2017_02_08_b':0.8*10**6,
                  'cubey_2017_02_08_l':0.8*10**6,
                  'cubey_2017_02_08_v':1.0*10**6,
                  'cubey_2017_02_08_af':0.8*10**6,
                  'cubey_2017_02_08_ap':0.8*10**6,
                  'cubey_2017_02_08_az':1.0*10**6,
                  'cubey_2017_02_08_bj':0.8*10**6,
                  'cubey_2017_02_08_bt':0.8*10**6,
                  'cubey_2017_02_08_cd':1.0*10**6,
}

default_strings = {'cubey_2017_01_15_a':r'1.36 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_01_31_a':r'1.36 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_01_31_aln':r'3.3 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_01_31_bxz':r'1.0 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_01_30_a':r'2.7 $\frac{W}{mK}$',
                   'cubey_2017_01_30_aln':r'2.7 $\frac{W}{mK}$',
                   'cubey_2017_01_30_bxz':r'2.0 $\frac{W}{mK}$',
                   'cubey_2017_01_30_dkl':r'0.325 $\frac{W}{mK}$',
                   'cubey_2017_02_02_b':r'2.6 $\frac{W}{mK}$',
                   'cubey_2017_02_02_l':r'1.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_v':r'2.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_af':r'2.6 $\frac{W}{mK}$',
                   'cubey_2017_02_02_ap':r'1.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_az':r'2.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_bj':r'2.6 $\frac{W}{mK}$',
                   'cubey_2017_02_02_bt':r'1.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_cd':r'2.0 $\frac{W}{mK}$',
                   'cubey_2017_02_02_cx':r'0.0 $\frac{m}{s}$',
                   'cubey_2017_02_02_dh':r'0.0 $\frac{m}{s}$',
                   'cubey_2017_02_02_dr':r'0.0 $\frac{m}{s}$',
                   'cubey_2017_02_08_b':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_l':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_v':r'1.0 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_af':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_ap':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_az':r'1.0 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_bj':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_bt':r'0.8 $10^6 \frac{J}{Km^3}$',
                   'cubey_2017_02_08_cd':r'1.0 $10^6 \frac{J}{Km^3}$',
}


# CUBEY: Measurement points ###################################################
obs_longlabels = {0:'North(out)',            # Outer ring
                  1:'Northwest(out)',
                  2:'West(out)',
                  3:'Southwest(out)',
                  4:'South(out)',
                  5:'Southeast(out)',
                  6:'East(out)',
                  7:'Northeast(out)',
                  8:'North(in)',            # Inner ring
                  9:'Northwest(in)',
                  10:'West(in)',
                  11:'Southwest(in)',
                  12:'South(in)',
                  13:'Southeast(in)',
                  14:'East(in)',
                  15:'Northeast(in)',
}

obs_shortlabels = {0:'NN',            # Outer ring
                   1:'NW',
                   2:'WW',
                   3:'SW',
                   4:'SS',
                   5:'SE',
                   6:'EE',
                   7:'NE',
                   8:'nn',            # Inner ring
                   9:'nw',
                   10:'ww',
                   11:'sw',
                   12:'ss',
                   13:'se',
                   14:'ee',
                   15:'ne',
}

obs_difflabels = {0:'NN-SS',    # Outer ring
                  1:'NW-SE',
                  2:'WW-EE',
                  3:'SW-NE',
                  4:'nn-ss',    # Inner ring
                  5:'nw-se',
                  6:'ww-ee',
                  7:'sw-ne'
}
