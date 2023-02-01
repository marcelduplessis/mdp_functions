from glob import glob
import xarray as xr
import numpy as np
from tqdm.notebook import tqdm


def load(sg_num, var, dataPath):

    filenames=sorted(glob(dataPath+'p'+str(sg_num)+'*.nc'))
    filenames
    
    for i,f in tqdm(enumerate(filenames)):
        
        ds = xr.open_dataset(f)
    
        ds_sg_data = ds[var]
        
        coords = ['log_gps_lon', 'log_gps_lat', 'log_gps_time']
        
        lon=ds[coords]['log_gps_lon'][1]
        lat=ds[coords]['log_gps_lat'][1]
        time=ds[coords]['log_gps_time'][1]
        
        dive = np.tile(np.array(f[63:66]).astype(float), ds_sg_data['ctd_time'].shape)
        
        ds_sg_data = (
                      ds_sg_data 
                          .assign_coords(dive         = ('sg_data_point', dive.astype(float)))          
                          .assign_coords(ctd_time     = ('sg_data_point', ds_sg_data.ctd_time.data))
                          .assign_coords(ctd_depth    = ('sg_data_point', ds_sg_data.ctd_depth.data))
                          .assign_coords(ctd_pressure = ('sg_data_point', ds_sg_data.ctd_pressure.data))
                          .swap_dims({"sg_data_point": "ctd_time"})
                          .assign_coords(lon_gps=lon)
                          .assign_coords(lat_gps=lat)
                          .assign_coords(time_gps=time)
                      )
        if i==0:
            ds_sg_data_main = ds_sg_data
                
        else:
            ds_sg_data_main = xr.concat([ds_sg_data_main, ds_sg_data], dim='ctd_time')
            
    ds_sg = ds_sg_data_main
    
    return ds_sg