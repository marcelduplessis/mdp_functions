from tqdm.notebook import tqdm  # Importing the tqdm library to display a progress bar
import matplotlib.dates as mdates  # Importing the matplotlib.dates module to work with dates
import numpy as np

def time_to_yearday(time):
    """
    Convert xarray time variable to year day values.
    
    Parameters:
    ----------
    time : An xarray time variable.
    
    Returns:
    -------
    yd : list
        A list of year day values corresponding to each time value.
    """
    
    yd = []  # Creating an empty list to store year day values
    
    for i in tqdm(range(time.size)):  # Looping through the time array using tqdm for progress bar
        
        t = time[i]  # Getting the current time
        
        year = t.dt.year  # Getting the year of the current time
        
        day0 = mdates.date2num(np.datetime64(str(year.values)+'-01-01 00:00:00'))  # Getting the date of the first day of the current year
        
        yd.append(mdates.date2num(t) - day0)  # Calculating the year day value for the current time and appending it to the yd list
    
    yd = np.array(yd)  # Converting the yd list to a numpy array
    
    return yd  # Returning the yd list of year day values
