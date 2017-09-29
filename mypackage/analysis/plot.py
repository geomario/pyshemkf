#!/usr/bin/python

# Plot routine for forward pics

import matplotlib as mpl
from matplotlib import cm            # Colormap commands (cm.get_cmap())
from matplotlib import colors
from matplotlib import pyplot as plt # ?
import numpy as np
import exceptions               # ?

from mypackage.run import pythonmodule as pm
from mypackage.plot import mycolors
from mypackage.plot import grids
from mypackage.plot import specs as sc

import arrays as aa
import variables as av

###############################################################################
#               Plot Nonuniform Image of Variable array                       #
###############################################################################

def plot(ax,
         model_name,
         dat,
         let,
         nt = 10,
         numpy_array_name = None,
         is_grid = True,
         is_mask = False,
         is_labels= True,
         is_ownticks = False,
         varname = 'kz_mean',                        #'head','v','temp','kz', 'uindex'
         v_component = 1,                           #0,1,2
         position = [0.1,0.1,0.6,0.8],
         is_ownlims = False,
         xlims = [0.0,620.0],
         ylims = [0.0,620.0],
         alpha = 1.0,
         maskvalue = 7,
         is_scatterplot = False,
         is_ownlocs = False,
         ownlocs = [[1,1,1]],
         loc_inds = range(16),
         marker = 'o',
         markersize=50,
         markercolor='red',
         markeralpha = 1.0,
         xlabelfontsize=40,
         ylabelfontsize=40,
         xownticks = [0.1+i*0.1 for i in range(9)],
         yownticks = [0.1+i*0.1 for i in range(9)],
         diff_ticks = 1,
         num_cbar = 7,
         low_cbar =  10.0285,
         high_cbar = 10.0304,
         auto_cbar = True,
         pic_format = 'pdf',                        # 'png','eps','pdf'
):
    """
    A plotting function for variable arrays in a NonUniformGrid.

    Parameters
    ----------
    ax : Axes
        The axes to draw to.

    model_name : string
        String of model name.

    dat : string
        String with date of model run.

    let : string
        String of letter of model run.

    nt : integer
        Number inside file name.

    numpy_array_name : string
        Full file name of numpy array including ending .npy

    Returns
    -------
    ax : Axes
        Axes containing image of variable array.

    pic_name : string
        Containing proposed saving location for Figure.
    """
    # Read grid arrays from mypackage/plot/grids.py
    x = grids.x(model_name,dat,let)
    y = grids.y(model_name,dat,let)
    xticks = grids.xticks(model_name,dat,let)[::diff_ticks]
    yticks = grids.yticks(model_name,dat,let)[::diff_ticks]

    # Load variable array
    if not numpy_array_name:
        var = np.load(pm.py_output_filename(av.tag,varname+'_'+str(nt).zfill(4),sc.specl(model_name,dat,let),"npy"))
    else:
        var = np.load(numpy_array_name)

    if varname == 'v':
        var = var[:,:,v_component]

    if auto_cbar:
        low_cbar = var.min()
        high_cbar = var.max()

    # # Possible Mask
    if is_mask:
        var = np.ma.array(var,mask = np.logical_or(var<maskvalue-0.5,var>maskvalue+0.5))

    # Axis position
    ax.set_position(position)

    # Create image
    im = mpl.image.NonUniformImage(ax,interpolation='nearest',
                                       cmap=mycolors.cmap_discretize(cm.viridis,num_cbar),
                                       norm = colors.Normalize(vmin=low_cbar,
                                                                   vmax=high_cbar,
                                                                   clip=False))
    im.set_data(x,y,var)
    im.set_alpha(alpha)
    ax.images.append(im)

    # Ticks
    if is_ownticks:
        ax.xaxis.set_ticks(xownticks)
        ax.yaxis.set_ticks(yownticks)
    else:
        ax.xaxis.set_ticks(xticks)
        ax.yaxis.set_ticks(yticks)

    # Grid
    if is_grid:
        ax.grid()

    # Monitoring Points
    if is_scatterplot:
        # Read
        if not is_ownlocs:
            locs = np.array(sc.locs(model_name,dat,let))
        else:
            locs = np.array(ownlocs)

        # Scatterplot
        ax.scatter(x[locs[loc_inds][:,0]-1],
                       y[locs[loc_inds][:,1]-1],
                       marker=marker,
                       c=markercolor,
                       edgecolors=markercolor,
                       alpha = markeralpha,
                       s=markersize)

    # Title
    # ax.set_title('Temperature field')

    # Labels
    ax.set_xlabel('[m]',fontsize=xlabelfontsize, visible=is_labels)
    ax.set_ylabel('[m]',fontsize=ylabelfontsize, visible=is_labels)
    ax.tick_params(length = 10 if is_labels else 0)
    ax.set_yticklabels(ax.get_yticks(),visible=is_labels)
    ax.set_xticklabels(ax.get_xticks(),visible=is_labels)

    # Axis Limits
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # Figure name
    if varname == 'v':
        varname = varname+'_'+str(v_component)
    if is_mask:
        varname = varname+'_'+str(maskvalue).zfill(2)

    pic_name = pm.py_output_filename(av.tag,varname+'_'+str(nt).zfill(4),sc.specl(model_name,dat,let),pic_format)

    return ax, pic_name


###############################################################################
#                    Add colorbar to figure with image                        #
###############################################################################

def cb(cb_ax,
       ax,
       varname = "kz_mean",
       varlabels = {'kz_mean':'Permeability [log(m2)]'},
       cb_ax_position = [0.8,0.1,0.03,0.8],
       labelsize = 20,
):
    """
    Add colorbar to figure.

    Parameters
    ----------
    cb_ax : Axes
        Empty colorbar-Axes instance.

    ax : Axes
        The axes holding the colored image.

    Returns
    -------
    cb_ax : Axes
        Colobar-Axes instance including the colorbar.
    """

    im = ax.images[0]

    # colorbar
    cb_ax.set_position(cb_ax_position)
    cb_ax.tick_params(labelsize = labelsize)
    cb_ax.set_title(varlabels[varname], y =1.02, fontsize=40)
    mpl.colorbar.Colorbar(cb_ax, im)

    return cb_ax