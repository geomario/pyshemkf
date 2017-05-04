#!/usr/bin/python

import numpy as np

from mypackage.run import runmodule as rm
from mypackage.run import pythonmodule as pm
from mypackage.plot import specs as sc
import mypackage.sensitivity.arrays as sa

###############################################################################
#               Plot temperature curves for different parameters              #
###############################################################################

def plot(ax,
             model_name,
             dat,
             let,
             imons = 9,
             title = 'Default',
             position = [0.1,0.1,0.9,0.9],
             pic_format = 'pdf',              # png, eps, pdf
             xlims = [10,30*24*3600],
             ylims = [11,20],
     ):
    """
    A plotting function for temperature curves in order to study
    sensitivity to different parameters.

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

    Returns
    -------
    ax : Axes
        Axes instance with plots.

    pic_name : string
        Containing proposed saving location for Figure.
    """

    sense = np.load(pm.py_output_filename(sa.tag,"sense",sc.specl(model_name,dat,let),"npy"))
    t = np.load(pm.py_output_filename(sa.tag,"truet",sc.specl(model_name,dat,let),"npy"))

    pic_name_start = 'sense_'+str(imons).zfill(2)

    # Default behavior
    deflet = rm.get_let_num(rm.get_num_let(let) + np.searchsorted(sa.varranges[sc.specl(model_name,dat,let)],
                                                                         sa.default_values[sc.specl(model_name,dat,let)]))
    deftemp = np.load(pm.py_output_filename(sa.tag,"truetemp",sc.specl(model_name,dat,deflet),"npy"))


    # Title
    if not title=="Default":
        ax.set_title(title,
                     size = 12)
    else:
        ax.set_title('Sensitivity: '+sa.sensitivity_varnames[sc.specl(model_name,dat,let)]
                     +' Unit: '+str(sa.unit_numbers[sc.specl(model_name,dat,let)])
                     +' ('+sa.unit_names[sa.unit_numbers[sc.specl(model_name,dat,let)]]+')',
                     size = 12)

    # Axis position
    ax.set_position(position)

    # Plot 
    for i in range(sense.shape[2]):
        ax.semilogx(t,sense[:,imons,i], 'o',
                    color = [1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2])], # White to black
                    markersize = 1.6,
                    markeredgewidth = 0.1)
    ax.semilogx(t,deftemp[:,imons], '-',
                color = 'black')

    # Labels
    ax.set_xlabel(r'Time',fontsize = 14, labelpad=0)
    ax.set_ylabel(r'Temperature [$ ^{\circ} C$]',fontsize = 14)
    ax.xaxis.set_ticks([10,60,600,3600,24*3600,10*24*3600])
    ax.xaxis.set_ticklabels(['10s','1min','10min','1h','1d','10d'])
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    # Text
    ax.text(0.95,0.95,
            "Range: "+sa.sensitivity_ranges[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)
    
    ax.text(0.95,0.85,
            "Default: "+sa.default_strings[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    # ax.text(0.95,0.75,
    #         "Measurement: "+sa.obs_longlabels[imons],
    #         fontsize=10,
    #         verticalalignment='top',
    #         horizontalalignment='right',
    #         transform=ax.transAxes)

    # Picture name
    pic_name = pm.py_output_filename(sa.tag,pic_name_start,sc.specl(model_name,dat,let),pic_format)
    
    return ax, pic_name


###############################################################################
#         Plot temperature difference curves for different parameters         #
###############################################################################

def dplot(ax,
          model_name,
          dat,
          let,
          imons = [1,9],
          pic_format = 'pdf',              # png, eps, pdf
          xlims = [10,30*24*3600],
          ylims = [0,10],
      ):

    pic_name_start = 'sense_'+str(imons[0]).zfill(2)+'_'+str(imons[1]).zfill(2)
    sense = np.load(pm.py_output_filename(sa.tag,"sense",sc.specl(model_name,dat,let),"npy"))
    t = np.load(pm.py_output_filename(sa.tag,"truet",sc.specl(model_name,dat,let),"npy"))

    # Default behavior
    deflet = rm.get_let_num(rm.get_num_let(let)
                            + np.searchsorted(sa.varranges[sc.specl(model_name,dat,let)],
                                              sa.default_values[sc.specl(model_name,dat,let)]))
    deftemp = np.load(pm.py_output_filename(sa.tag,"truetemp",sc.specl(model_name,dat,deflet),"npy"))


    ax.set_title('Sensitivity of Temperature-Difference at '+str(imons[0]) +' minus '
                 + str(imons[1]) +': '
                 +sa.sensitivity_varnames[sc.specl(model_name,dat,let)]
                 +' Unit: '+str(sa.unit_numbers[sc.specl(model_name,dat,let)])
                 +' ('+sa.unit_names[sa.unit_numbers[sc.specl(model_name,dat,let)]]+')',
                 size = 8)

    # Plot
    for i in range(sense.shape[2]):
        ax.semilogx(t,sense[:,imons[0],i]-sense[:,imons[1],i], 'o',
                    color = [1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2]),
                             1.0-i/float(sense.shape[2])], # White to black
                    markersize = 1.6,
                    markeredgewidth = 0.1)
    ax.semilogx(t,deftemp[:,imons[0]]-deftemp[:,imons[1]], '-',
                color = 'black')

    ax.set_xlabel(r'Time',fontsize = 14, labelpad=0)
    ax.set_ylabel(r'Temperature Difference [$ ^{\circ} C$]',fontsize = 14)
    ax.xaxis.set_ticks([10,60,600,3600,24*3600,10*24*3600])
    ax.xaxis.set_ticklabels(['10s','1min','10min','1h','1d','10d'])
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    ax.text(0.95,0.95,
            "White->Black: "+sa.sensitivity_ranges[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    ax.text(0.95,0.85,
            "Default: "+sa.default_strings[sc.specl(model_name,dat,let)],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    ax.text(0.95,0.75,
            "Measurement 1: "+sa.obs_longlabels[imons[0]],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)

    ax.text(0.95,0.65,
            "Measurement 2: "+sa.obs_longlabels[imons[1]],
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='right',
            transform=ax.transAxes)
    

    pic_name = pm.py_output_filename(sa.tag,pic_name_start,sc.specl(model_name,dat,let),pic_format)
    
    return ax, pic_name

###############################################################################
#               Plot sensitiviy curves for different parameters               #
###############################################################################

def nplot(ax,model_name,dat,let,
          imons = 9,
          pic_format = 'pdf',              # png, eps, pdf
          xlims = [100,30*24*3600],
          ylims = [-0.01,0.15],
      ):

    pic_names = ['numsense_'+str(imons).zfill(2)]
    numsense = np.load(pm.py_simple_output_filename("numsense_"+str(imons).zfill(2),
                                                    sa.tag,
                                                    "npy"))
    numsense_labels = np.load(pm.py_simple_output_filename("numsense_labels_"+str(imons).zfill(2),
                                                    sa.tag,
                                                    "npy"))
    t = np.load(pm.py_output_filename(sa.tag,
                                      "truet",
                                      sc.specl(sc.model_name,sc.dat,sc.lets[0]),
                                      "npy"))

    ax.set_title('Sensitivity numbers at '+sa.obs_longlabels[imons],# +sa.sensitivity_varnames[sc.spec()]
                 # +' Unit: '+str(sa.unit_numbers[sc.spec()])
                 # +' ('+sa.unit_names[sa.unit_numbers[sc.s,pec()]]+')',
                 size = 20)

    # Plot
    for i in range(numsense.shape[1]):
        ax.semilogx(t,numsense[:,i], 'o',
                    color = [i*0.3,i*0.3,i*0.3], # White to black
                    # color = 'black',
                    linestyle = '--',
                    label=numsense_labels[i],
                    markersize = 0.0,
                    markeredgewidth = 0.1)

    ax.axhline(0,c='k',linestyle=':',linewidth=0.3)
    ax.set_xlabel(r'Time',fontsize = 14, labelpad=0)
    ax.set_ylabel(r'Temperature difference [$ ^{\circ} C$]',fontsize = 14)
    ax.xaxis.set_ticks([10,60,600,3600,24*3600,10*24*3600])
    ax.xaxis.set_ticklabels(['10s','1min','10min','1h','1d','10d'])
    ax.set_xlim(xlims[0],xlims[1])
    ax.set_ylim(ylims[0],ylims[1])

    ax.legend(markerscale=2.0,
              loc = 'upper left',
              fontsize=6,
              ncol=3)
          
    pic_name = pm.py_output_filename(sa.tag,pic_names[0],sc.specl(model_name,dat,let),pic_format)
          
    return ax, pic_name
