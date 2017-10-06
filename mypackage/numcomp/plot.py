#!/usr/bin/python

# Plot routine for numcomp pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
from matplotlib import mlab

import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import plotarrays as pa
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as na

def plot(ax,
         which_methods,
         which_methods_left,
         which_methods_right,
         which_res = 'endres',
         model = 'wavebc',
         n_runs = 1000,
         method = 'ttest',
         enssize = 50,
         n_syn = 1,                       #number of synthetic studies
         n_syn_bold = 1,
         n_comparisons = 10000,
         pic_format = 'pdf',
         bar_colors = ['black','white','grey'],
):

    """
    Reads probability arrays which method is better,
    worse, or if they are even. Then plots those
    three possibilities in bars comparing the methods
    given in which_methods_left and which_methods_right.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    which_methods : array int
        Array of integers containing the method specifiers
        from module plotarrays.

    which_methods_left : array int
        Array of integers containing the method specifiers
        for the left side of the comparisons.

    which_methods_right : array int
        Array of integers containing the method specifiers
        for the right side of the comparisons.

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    method : string
        Which method to use for statistical comparison
        of the subset. If n_syn == 1, the comparison
        always defaults to comparing the residuals.
        'ttest' - Use the T-Test, testing if the
                  two samples belong to the same
                  Gaussian distribution.
        'gauss' - Calculate Gaussian distribution
                  of the difference and calculate
                  its probability to be larger
                  than zero.

    enssize : integer
        Ensemble size of the job. Possibilities: 50,
        70, 100, 250, 500, 1000, 2000

    n_syn : integer
        Number of synthetic studies in subset.

    n_syn_bold : integer
        Number of synthetic studies in subset used for
        the bold ticklabels.

    n_comparisons : integer
        Number of comparisons calculated.

    pic_format : string
        Format of the picture
        'pdf' - pdf-format
        'eps' - eps-format
        'png' - png-format
        'jpg' - jpg-format
        'svg' - svg-format

    bar_colors : array of strings
        Three colors for the three patches of one bar.

    Returns
    -------
    ax : array
        Axes containing plot.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Check
    for imethod in which_methods_left:
        if not imethod in which_methods:
            raise exceptions.RuntimeError('Wrong methods in wrong_methods_left')
    for imethod in which_methods_left:
        if not imethod in which_methods:
            raise exceptions.RuntimeError('Wrong methods in wrong_methods_right')

    if n_runs==1000:
        if not enssize in [50,70,100,250]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>1000:
            raise exceptions.RuntimeError('n_syn wrong')
    else:
        if not enssize in [500,1000,2000]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>100:
            raise exceptions.RuntimeError('n_syn wrong')

    # Both methods in one array
    show_methods = [which_methods_left,
                        which_methods_right]
    # Number of bars and patches
    num_bars = len(show_methods[0])
    num_patches = 3*num_bars

    # Load probs
    probs = np.load(pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+str(n_comparisons)+'_'+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Load probs for bold labels
    probs_bold = np.load(pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn_bold)+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    ax.set_position([0.3,0.05,0.4,0.75])
    ax.set_frame_on(False)

    # Patch arrays for ax.barh()
    in_bottom = np.zeros(num_patches)
    in_height = np.zeros(num_patches)
    in_width = np.zeros(num_patches)
    in_left = np.zeros(num_patches)
    in_color = ['' for i in range(num_patches)]
    for i in range(num_patches):
        in_bottom[i] = num_bars-i/3
        in_height[i] = 0.8
        in_width[i] = probs[show_methods[0][i/3],
                            show_methods[1][i/3]][np.mod(i,3)]
        in_left[i] = np.sum(probs[show_methods[0][i/3],
                                  show_methods[1][i/3]][0:np.mod(i,3)])
        in_color[i] = bar_colors[np.mod(i,3)]

    # Plot patches in bars
    ax.barh(bottom = in_bottom,
            height = in_height,
            width = in_width,
            left = in_left,
            color = in_color,
            edgecolor = 'k')

    # H_0 labels inside bar
    if method == "ttest":
        for i in range(1,num_bars+1):
            if in_left[3*i-1]-in_left[3*i-2] > 0.15:
                ax.text(in_left[3*i-2]   +0.4*(in_left[3*i-1]-in_left[3*i-2]),
                        in_bottom[3*i-2] +0.3,
                        "$H_0$",
                        fontsize = 20)

    # Axis 1
    ax.tick_params(direction = 'out', length = 0,
                   width = 1, labelsize = 20,
                   top = 'off', bottom = 'off',
                   labelright = 'off',
                   pad = 8)
    ax.set_xlim([-0.01,1.01])
    ax.set_ylim([0.9,num_bars+0.8])
    ax.set_xticks([])
    ax.set_yticks([num_bars-i +0.4 for i in range(num_bars)])
    ax.set_yticklabels([pa.longnames_methods[show_methods[0][i]] for i in range(num_bars)])

    # Twin Axis 2
    ax2 = ax.twinx()
    ax2.set_position([0.3,0.05,0.4,0.75])
    ax2.set_frame_on(False)
    ax2.tick_params(direction = 'out', length = 0,
                   width = 1, labelsize = 20,
                   top = 'off', bottom = 'off',
                   labelleft = 'off',labelright = 'on',
                   labelcolor = 'black',
                   pad = 8)
    ax2.set_xlim([-0.01,1.01])
    ax2.set_ylim([0.9,num_bars+0.8])
    ax2.set_xticks([])
    ax2.set_yticks([num_bars-i +0.4 for i in range(num_bars)])
    ax2.set_yticklabels([pa.longnames_methods[show_methods[1][i]] for i in range(num_bars)])

    # Boldness of axislabels
    for i in range(num_bars):
        if(probs_bold[show_methods[0][i],show_methods[1][i]][0] == 1):
            ax.yaxis.get_majorticklabels()[i].set_weight('bold')
        elif(probs_bold[show_methods[0][i],show_methods[1][i]][2] == 1):
            ax2.yaxis.get_majorticklabels()[i].set_weight('bold')
        else:
            ax.yaxis.get_majorticklabels()[i].set_style('italic')
            ax2.yaxis.get_majorticklabels()[i].set_style('italic')

    # Saving location
    pic_name = pm.py_output_filename(na.tag,'bars_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+str(n_comparisons)+'_'+'_'+'_'.join([str(i) for i in which_methods]),pic_format)

    return ax, pic_name

def matrix(ax,
         which_methods = [0,1,2,3,4,5,6],
         indsorts = [1,6,5,4,3,2,0] ,
         which_res = 'endres',
         method = 'ttest',
         n_runs = 1000,
         model = 'wavebc',
         enssize = 50,
         n_syn = 1,                       #number of synthetic studies
         n_comparisons = 10000,
         pic_format = 'pdf',      #'png' or 'eps' or 'svg' or 'pdf'
         # figpos = [0.15,0.3,0.8,0.6],               #xbeg, ybeg, xrange, yrange
         # ylims = [0.28,0.82],
         ticksize = 20,
         xtick_y = 0.0,
         # num_pack = 4,                     # Number of methods in pack
         # formatsos = ['o','v','s','p','o','v','s','p'],
         # coleros = [(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0),
         #                (1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0),(1.0,1.0,1.0)],
         # markersize = 10,
         # markeredgesize = 1.5,
         # fontleg = 30,                              #18
         # fonttit = 40,
         # fontlab = 40,
         # fonttic = 30,
             ):
    """
    A plotting function for statistics of residual distributions.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    which_methods : array of ints
        The methods to be loaded in ascending order.

    indsorts : array of ints
        The methods to included in own this order.

    which_res : string
        'endres' - use residuals after EnKF run
        'begres' - use residuals before EnKF run

    method : string
        Which method to use for statistical comparison
        of the subset. If n_syn == 1, the comparison
        always defaults to comparing the residuals.
        'ttest' - Use the T-Test, testing if the
                  two samples belong to the same
                  Gaussian distribution.
        'gauss' - Calculate Gaussian distribution
                  of the difference and calculate
                  its probability to be larger
                  than zero.

    n_runs : integer
        1000 - typically exist for ensemble sizes 50, 70, 100, 250
        100 - typically exist for ensemble sizes 500, 1000, 2000

    model : string
        'wavebc' - Model wavebc
        'wave' - Model wave

    enssize : integer
        Ensemble size of the job. Possibilities: 50,
        70, 100, 250, 500, 1000, 2000

    n_syn : integer
        Number of synthetic studies in subset.

    n_comparisons : integer
        Number of comparisons calculated.

    pic_format : string
        Format of the picture
        'pdf' - pdf-format
        'eps' - eps-format
        'png' - png-format
        'jpg' - jpg-format
        'svg' - svg-format

    Returns
    -------
    ax : Axes
        Axes containing plot.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    # Check
    for imethod in indsorts:
        if not imethod in which_methods:
            raise exceptions.RuntimeError('Wrong methods in indsorts')

    if n_runs==1000:
        if not enssize in [50,70,100,250]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>1000:
            raise exceptions.RuntimeError('n_syn wrong')
    else:
        if not enssize in [500,1000,2000]:
            raise exceptions.RuntimeError('enssize wrong')
        if n_syn>100:
            raise exceptions.RuntimeError('n_syn wrong')

    # Number of compared methods
    num_methods = len(indsorts)

    # Load probs
    probs = np.load(pm.py_output_filename(na.tag,'probs_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+'_'+str(n_comparisons)+'_'+'_'.join([str(i) for i in which_methods]),'npy'))

    # Sort probs
    probs = probs[indsorts,:,:]
    probs = probs[:,indsorts,:]

    ax.set_position([0.32,0.2,0.6,0.8])

    # Rectangles in upper right half: Fraction of Undecided
    undecided = probs[:,:,1]
    for ipm in range(num_methods):
        for jpm in range(num_methods):
            if ipm > jpm:
                # Lower left half white
                undecided[ipm,jpm] = None
            if ipm == jpm:
                # Diagonal black
                undecided[ipm,jpm] = 1.0
            if ipm < jpm:
                # Single comparisons white
                if n_syn == 1:
                    undecided[ipm,jpm] = None
                # One comparison white
                if n_syn == 1000:
                    undecided[ipm,jpm] = None


    ax.imshow(undecided,interpolation='nearest',cmap='Greys',
              norm = colors.Normalize(vmin=0,vmax=1,clip=False))

    # Triangles: Grid
    X,Y = np.meshgrid(np.arange(8),np.arange(8))
    X = X.flatten()-0.5
    Y = Y.flatten()-0.5

    # Triangles: Indices
    triangles = np.array([[j*8,1+j*8,8+j*8] for j in range(1,num_methods)]
                             +[[1+j*8, 2+j*8, 9+j*8] for j in range(2,num_methods)]
                             +[[2+j*8, 3+j*8,10+j*8] for j in range(3,num_methods)]
                             +[[3+j*8, 4+j*8,11+j*8] for j in range(4,num_methods)]
                             +[[4+j*8, 5+j*8,12+j*8] for j in range(5,num_methods)]
                             +[[5+j*8, 6+j*8,13+j*8] for j in range(6,num_methods)]
                             +[[1+j*8, 8+j*8, 9+j*8] for j in range(1,num_methods)]
                             +[[2+j*8, 9+j*8,10+j*8] for j in range(2,num_methods)]
                             +[[3+j*8,10+j*8,11+j*8] for j in range(3,num_methods)]
                             +[[4+j*8,11+j*8,12+j*8] for j in range(4,num_methods)]
                             +[[5+j*8,12+j*8,13+j*8] for j in range(5,num_methods)]
                             +[[6+j*8,13+j*8,14+j*8] for j in range(6,num_methods)])

    # Triangles: Triangulation instance
    tria = mpl.tri.Triangulation(X,Y,triangles)

    # Triangles: Colors
    coleros = np.array([[probs[i,j,0] for i in range(j+1,num_methods)] for j in range(6)]
                           +[[probs[i,j,2] for i in range(j+1,num_methods)] for j in range(6)])
    coleros = np.hstack(coleros)

    # Triangles: Plot with facecolor
    plt.tripcolor(tria,facecolors=coleros,
                    cmap=mpl.cm.Greys,
                    norm = colors.Normalize(vmin=0,vmax=1,clip=False),
                    edgecolor='k')

    # Plot: Mostly ticks
    ax.set_xticks([i for i in range(num_methods)])
    ax.set_xticklabels([pa.names_methods[indsorts[i]] for i in range(num_methods)], fontsize=ticksize,
                       rotation=90,y=xtick_y)
    ax.set_yticks([i for i in range(num_methods)])
    ax.set_yticklabels([pa.names_methods[indsorts[i]] for i in range(num_methods)], fontsize=ticksize)
    ax.tick_params(length=0)
    ax.set_frame_on(False)

    # Text: Upper triangles
    for i in range(3):
        for itext in range(num_methods):
            for jtext in range(num_methods):
                if itext<jtext:
                    ntext = 100*probs[jtext,itext,i] if i!=1 else 100*probs[itext,jtext,i]
                    ttext = str(ntext)[0:4] if ntext<100 else str(ntext)[0:3]
                    px = itext-0.35 if i==0 else (jtext-0.125 if i==1 else itext-0.05)
                    py = jtext-0.15 if i==0 else (itext+0.05  if i==1 else jtext+0.3 )
                    colero = 'white' if ntext>50 else 'black'

                    if i!=1 or n_syn!=1000:
                        ax.text(px,py,ttext,color = colero,fontsize = 10)



    # Saving location
    pic_name = pm.py_output_filename(na.tag,'matrix_'+which_res,model+'_'+str(n_runs)+'_'+method+'_'+str(enssize)+'_'+str(n_syn)+'_'+str(n_comparisons)+'_'+'_'.join([str(i) for i in which_methods]),pic_format)

    return ax, pic_name
