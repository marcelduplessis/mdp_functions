import math
import numpy as np

def getWindDir(uwind, vwind):
    
    data_dir = []
    
    for i in range(len(uwind)):
        data_dir += math.atan2(vwind[i], uwind[i])/math.pi*180,

    data_dir = np.array(data_dir)
    
    return data_dir

def setWindDirZero360(wind_dir):

    ind1 = np.nonzero((wind_dir > 0)    & (wind_dir < 90))
    ind2 = np.nonzero((wind_dir > 90)   & (wind_dir < 190))
    ind3 = np.nonzero((wind_dir > -180) & (wind_dir < -90))
    ind4 = np.nonzero((wind_dir > -90)  & (wind_dir < 0))
    
    wind_dir[ind1] = 90 - wind_dir[ind1]
    wind_dir[ind2] = 450 - wind_dir[ind2]
    wind_dir[ind3] = abs(wind_dir[ind3] - 90)
    wind_dir[ind4] = abs(wind_dir[ind4]) + 90
    
    return wind_dir