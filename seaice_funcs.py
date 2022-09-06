import xarray as xr
from scipy.interpolate import griddata as g
from tqdm import tqdm
import numpy as np
import pandas as pd

def read_AMSR2_seaice(dataPath):

    seaice = xr.open_mfdataset(dataPath+'asi-AMSR2-s6250-201*.hdf', 
                               concat_dim='time', combine='nested',
                               engine="netcdf4")
    
    seaice_lnlt = xr.open_dataset(dataPath+'LongitudeLatitudeGrid-s6250-Antarctic.hdf',
                                  engine='netcdf4'
                                 )
    
    seaice['time'] = (('time'), pd.date_range(start='2018-07-01', end='2019-03-31', freq='D'))
    
    seaice = seaice.rename({'ASI Ice Concentration': 'si_conc'})
    seaice = seaice.assign_coords(lon=(["x", "y"], np.array(seaice_lnlt.Longitudes)))
    seaice = seaice.assign_coords(lat=(["x", "y"], np.array(seaice_lnlt.Latitudes)))
    seaice = seaice.assign(si=(["time", "x", "y"], seaice.si_conc.values))
    seaice = seaice.drop('si_conc')
    
    return seaice


def regrid_linear(seaice, xnew=np.arange(-180, 180.1, 0.1), ynew=np.arange(-75, -49.9, 0.1)):
    

    X = xnew # your longitudes you want to grid to
    Y = ynew # your latitudies you want to grid to
    
    x, y = np.meshgrid(xnew,ynew)
    
    sic_new = np.ndarray([len(seaice.si), len(ynew), len(xnew)]) # setting a new sic array
    
    x_, y_ = np.ravel(seaice.lon), np.ravel(seaice.lat)
    x_[x_>180] = x_[x_>180]-360
    
    for i in tqdm(range(len(seaice.si))):
    
        si = np.ravel(seaice.si[i, :, :].values)
        sic_new[i, :, :] = g((y_, x_), si, (y, x), method='nearest')
         
    sic_new[sic_new==0] = np.NaN
    sic_new = np.ma.masked_invalid(sic_new)
    
    sic = xr.Dataset(data_vars={'sic' : (('time', 'lat', 'lon'), sic_new)},
                     coords={'time' : seaice.time, 
                             'lat'  : ynew, 
                             'lon'  : xnew})
    
    return sic


def process_AMSR2(dataPath, outPath, outName='sic_interp.nc'): # choose the datapath where the files currently are sitting
    
    print('Step 1/3: Beginning the processing of sea ice...')
        
    # read in the AMSR2 sea ice data
    seaice = read_AMSR2_seaice(dataPath)
    
    print('Step 2/3: Data has been loaded in, beginning with regridding...')
    
    # regrid the curvilinear grid to linear
    sic = regrid_linear(seaice)
    
    print('Step 3/3: Regridding complete, now saving...')
    
    # save the sic data to netcdf so that you don't have to go through this slow process again
    sic.to_netcdf(outPath+outName)
    
    print('Processing completed, saved as '+str(outName)+' in directory '+str(outPath))
    
    return