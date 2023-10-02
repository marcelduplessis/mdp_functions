import datetime
import numpy as np
import matplotlib.dates as mdates

def pydate2matdate(dt):
    
    matdate1970 = 719529
    
    return matdate1970 + mdates.date2num(dt) 

def matdate2pydate(dt):
    
    py_datetime = [np.datetime64(datetime.datetime.fromordinal(int(d)) + datetime.timedelta(days=d % 1) - datetime.timedelta(days=366), 'ms') for d in dt]
    
    return np.array(py_datetime)
    