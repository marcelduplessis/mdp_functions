import xarray as xr
import os
import pathlib

def read_sd(path):

    files = list(pathlib.Path(path).glob('saildrone*.nc'))
    files.sort()
    
    dat = ['WIND_FROM_MEAN',
           'WIND_FROM_STDDEV',
           'WIND_SPEED_MEAN',
           'WIND_SPEED_STDDEV',
           'UWND_MEAN',
           'UWND_STDDEV',
           'VWND_MEAN',
           'VWND_STDDEV',
           'WWND_MEAN',
           'WWND_STDDEV',
           'GUST_WND_MEAN',
           'GUST_WND_STDDEV',
           'WIND_MEASUREMENT_HEIGHT_MEAN',
           'WIND_MEASUREMENT_HEIGHT_STDDEV',
           'TEMP_AIR_MEAN',
           'TEMP_AIR_STDDEV',
           'RH_MEAN',
           'RH_STDDEV',
           'BARO_PRES_MEAN',
           'BARO_PRES_STDDEV',
           'PAR_AIR_MEAN',
           'PAR_AIR_STDDEV',
           'LW_IRRAD_MEAN',
           'LW_IRRAD_STDDEV',
           'SW_IRRAD_TOTAL_MEAN',
           'SW_IRRAD_TOTAL_STDDEV',
           'SW_IRRAD_DIFFUSE_MEAN',
           'SW_IRRAD_DIFFUSE_STDDEV',
           'TEMP_IR_SEA_WING_UNCOMP_MEAN',
           'TEMP_IR_SEA_WING_UNCOMP_STDDEV',
           'WAVE_DOMINANT_PERIOD',
           'WAVE_SIGNIFICANT_HEIGHT',
           'TEMP_DEPTH_HALFMETER_MEAN',
           'TEMP_DEPTH_HALFMETER_STDDEV',
           'TEMP_SBE37_MEAN',
           'TEMP_SBE37_STDDEV',
           'SAL_SBE37_MEAN',
           'SAL_SBE37_STDDEV',
           'COND_SBE37_MEAN',
           'COND_SBE37_STDDEV',
           'O2_CONC_SBE37_MEAN',
           'O2_CONC_SBE37_STDDEV',
           'O2_SAT_SBE37_MEAN',
           'O2_SAT_SBE37_STDDEV',
           'CHLOR_WETLABS_MEAN',
           'CHLOR_WETLABS_STDDEV',
           'XCO2_DRY_SW_MEAN_ASVCO2',
           'XCO2_DRY_AIR_MEAN_ASVCO2'
          ]
    
    # Loading the files
    
    tmp = []
    for i in range(len(files)):
        # [dat] chooses just the data variables. The files had a mismatch in the available variables.
        tmp.append(xr.open_dataset(files[i],engine='netcdf4').sel(trajectory=1067).swap_dims({'obs':'time'})[dat]) 
    ds = xr.concat(tmp,dim='time')
    
    return ds

