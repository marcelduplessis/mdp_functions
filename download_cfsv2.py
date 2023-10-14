import numpy as np
from tqdm import tqdm
from siphon.catalog import TDSCatalog
import xarray as xr
from siphon.ncss import NCSS
from netCDF4 import NetCDF4DataStore

def download_cfsv2_monthly_data(path, variables, years, months):
    """
    Download CFSv2 monthly data for specified variables, years, and months.

    Args:
        path (str): The directory where the downloaded NetCDF files will be saved.
        variables (list): List of variable names to download.
        years (list): List of years for which to download data.
        months (list): List of months (1-12) for which to download data.

    Example:
        path = '/Users/xduplm/Google Drive/My Drive/data/reanalysis/cfsv2/'
        variables = [
            'Sensible_heat_net_flux_surface_Mixed_intervals_AverageAvg-6hourIntv',
            'Latent_heat_net_flux_surface_Mixed_intervals_AverageAvg-6hourIntv',
            # Add more variable names as needed
        ]
        years = np.arange(2012, 2023, 1)
        months = np.arange(1, 13, 1)

        download_cfsv2_monthly_data(path, variables, years, months)
    """

    # Iterate over the specified years
    for year in years:
        year_str = str(year)
        
        # Iterate over the specified months
        for month in months:
            month_str = f'{month:02}'  # Format month as zero-padded string

            # Construct THREDDS catalog URL for the specific year and month
            catalog_url = f'https://www.ncei.noaa.gov/thredds/catalog/model-cfs_v2_anl_mm_flxf/{year_str}/{year_str}{month_str}/catalog.xml'

            # Create a TDSCatalog object for the catalog URL
            cat = TDSCatalog(catalog_url)

            # Access the dataset
            dataset = cat.datasets['flxf00.gdas.' + year_str + month_str + '.grib2']

            print('Downloading:', 'flxf00.gdas.' + year_str + month_str + '.grib2')

            # Create an NCSS object and query
            ncss = dataset.subset()
            query = ncss.query()
            query.lonlat_box(north=0, south=-90, east=360, west=0)

            # Specify the variables to download
            query.variables(*variables)

            # Get the data from the server
            cfs = ncss.get_data(query)

            # Open the dataset and save it to a NetCDF file
            ds = xr.open_dataset(NetCDF4DataStore(cfs))
            ds.to_netcdf(f'{path}cfsv2_flxf00_{year_str}{month_str}.nc')
