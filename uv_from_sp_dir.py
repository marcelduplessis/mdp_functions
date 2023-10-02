# __init__.py

import numpy as np

def uv_from_sp_dir(speed, direction):
    
    md = 270 - direction
    md[md<0] = md[md<0]+360
    
    u = (speed) * np.cos(np.deg2rad(md))
    v = (speed) * np.sin(np.deg2rad(md))
    
    return -u,-v