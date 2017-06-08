import numpy as np
import exceptions

###############################################################################
#                      Variables for Sensitivity Analysis                     #
###############################################################################

tag = "sensitivity"

# Quartz and Water
lam_quartz = 7.0
lam_water = 0.59
rc_quartz = 1.97*10**6
rc_water = 4.186*10**6

# Sensitivity ranges
lam_smin = 2.3
lam_smax = 3.7
lam_cmin = 1.5
lam_cmax = 2.5

rc_smin = 2.52*10**6
rc_smax = 2.96*10**6
rc_cmin = 1.2*10**6
rc_cmax = 2.2*10**6

###############################################################################
#                             Diffusivity calculation                         #
###############################################################################

def alpha(
        uindex,
        length = 1000,
        ):
    """
    Calculating thermal diffusivity for Units 1,2 (sand) and 7 (concrete/cement).
    Unit: m2/s

    Parameters
    ----------
    uindex : integer
        Unit Index in CUBEY-model

    Returns
    -------
    alpha : array
        Thermal diffusivity values for porosities between 0 and 1.
    """

    if uindex in [1,2]:
        # Porosity
        phi = np.linspace(1.0/length,1,length)

        # Thermal conductivity and volumetric heat capacity
        lam = lam_quartz**(1-phi) * lam_water**phi
        rc = rc_quartz*(1-phi) + rc_water*phi

        # Thermal diffusivity
        alpha = lam/rc

    elif uindex in [7]:
        # Scaling variable (Not porosity, just linear interpolation between extremes)
        sca = np.linspace(1.0/length,1,length)

        # Min and Max diffusivities
        alpha_min = lam_cmin/rc_cmax
        alpha_max = lam_cmax/rc_cmin

        alpha = alpha_min*(1-sca) + alpha_max*sca

    else:
        raise exceptions.RuntimeError("uindex must be 1,2 or 7")
        
    return alpha

