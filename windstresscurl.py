def wind_stress_curl(Tx, Ty, x, y):
    
    """Calculate the curl of wind stress (Tx, Ty).
    Args:
        Tx, Ty: Wind stress components (N/m^2), 3d
        x, y: Coordinates in lon, lat (degrees), 1d.
    Notes:
        Curl(Tx,Ty) = dTy/dx - dTx/dy
        The different constants come from oblateness of the ellipsoid.
        Ensure the coordinates follow tdim=0, ydim=1, xdim=2
    """
    
    dy = np.abs(y[1] - y[0]) # scalar in deg
    dx = np.abs(x[1] - x[0]) 
    
    dy *= 110575. # scalar in m
    dx *= 111303. * np.cos(y * np.pi/180) # array in m (varies w/lat)
        
    dTxdy = np.gradient(Tx, dy, axis=1) # (N/m^3)
    dTydx = np.ndarray(Ty.shape)
    
    for i in range(len(y)):
        
        dTydx[:,i,:] = np.gradient(Ty[:,i,:], dx[i], axis=1)

    curl_tau = dTydx - dTxdy # (N/m^3)
    
    return curl_tau