import cdsapi
from urllib.request import urlopen# start the client

def download_era5_cdsapi(var, day, month, year, dataset="reanalysis-era5-single-levels", path=''):
    
    cds = cdsapi.Client()# dataset you want to read

    params = {
              'variable': [var],
              'product_type': 'reanalysis',
              'year': [year],
              'month': [month],
              'day': day,
              'time': [
                       '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                       '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
                       '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                       '21:00', '22:00', '23:00'
                      ],
              'area': [
                       '0', '0', '-90', '360'
                      ],
              'format': 'netcdf'
             }
    
    fl = cds.retrieve(dataset, params) # download the file 
    
    fl.download(path+str(var)+'_'+str(year)+str(month)+'.nc') # load into memory
        
    return