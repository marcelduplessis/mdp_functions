import numpy as np
import gsw
import matplotlib.pyplot as plt

def ts_plot(ax, smin, smax, tmin, tmax):
 
    # Figure out boudaries (mins and maxs)
    smin = smin - (0.01 * smin)
    smax = smax + (0.01 * smax)
    tmin = tmin - (0.1 * tmin)
    tmax = tmax + (0.1 * tmax)
     
    # Calculate how many gridcells we need in the x and y dimensions
    xdim = int(np.round((smax-smin)/0.1+1,1))
    ydim = int(np.round((tmax-tmin)+1,1))
     
    # Create empty grid of zeros
    dens = np.zeros((int(ydim),int(xdim)))
     
    # Create temp and salt vectors of appropiate dimensions
    ti = np.linspace(1,ydim-1,ydim)+tmin
    si = np.linspace(1,xdim-1,xdim)*0.1+smin
     
    # Loop to fill in grid with densities
    for j in range(0,int(ydim)):
        for i in range(0, int(xdim)):
            dens[j,i]=gsw.rho(si[i],ti[j],0)
     
    # Substract 1000 to convert to sigma-t
    dens = dens - 1000
     
    # Plot data ***********************************************
    
    CS = ax.contour(si,ti,dens, linestyles='solid', colors='0.5')
    ax.clabel(CS, fontsize=16, inline=1, fmt='%1.1f') # Label every second level
    
    return ax