import struct
import numpy as np
import pandas as pd
import moxa_conversions as mc


def read_gill_sonic(fname):
    
    """
    Reads in binary data from a Gill Sonic R3A anemometer and extracts the time, u_wind, v_wind, w_wind, and t_sos.
    
    The binary file must contain data in chunks of 30 bytes.

    Author: [Marcel du Plessis, marcel.du.plessis@gu.se]
    Date: [24 February 2023]

    Args:
        fname (str): Filepath to binary data file.

    Returns:
        time (np.ndarray): Array of datetime64[ms] timestamps.
        u_m (np.ndarray): Array of u-wind speeds in m/s.
        v_m (np.ndarray): Array of v-wind speeds in m/s.
        w_m (np.ndarray): Array of w-wind speeds in m/s.
        t_sos (np.ndarray): Array of temperature values in degrees Celsius.
    """
    
    time_string = []
    u_m   = []
    v_m   = []
    w_m   = []
    t_sos = []

    # Open binary file for reading
    with open(fname, "rb") as f:
        
        # Chunk size (in bytes)
        chunk_size = 30
        
        # Read in first chunk
        chunk = f.read(chunk_size)
        
        # Loop through chunks until end of file
        while chunk:
    
            # Read in next chunk
            chunk = f.read(chunk_size)
            
            # If chunk is empty, skip to next iteration
            if chunk == b'': 
                continue     
            
            # Extract timestamp from chunk
            time_str = '20' + str(chunk)[2:4] + '-' + str(chunk)[4:6] + '-' + str(chunk)[6:8] + ' ' + str(chunk)[8:10] + ':' + str(chunk)[10:12] + ':' + str(chunk)[12:18],
            
            # Try to extract remaining data from chunk
            try:
                
                # convert the time string to a datetime object
                time = np.array(time_str, dtype='datetime64[ms]')                
                
                # Extract remaining data using struct.unpack
                u_wind, = struct.unpack('!h', chunk[21:23])
                v_wind, = struct.unpack('!h', chunk[23:25])
                w_wind, = struct.unpack('!h', chunk[25:27])
                tm_sos, = struct.unpack('!h', chunk[27:29])
                
                # Append timestamp to list
                time_string.append(time_str)
                
                # Append data to lists
                u_m.append(u_wind)
                v_m.append(v_wind)
                w_m.append(w_wind)
                t_sos.append(tm_sos)
            
            # If there is an error extracting data, skip to next iteration
            except:                
                continue
        
    # Convert lists to numpy arrays
    time = np.array(time_string, dtype='datetime64[ms]')
    time = np.squeeze(time)
    
    u_m = np.array(u_m)/100
    v_m = np.array(v_m)/100
    w_m = np.array(w_m)/100
    t_sos = np.array(t_sos)/100-273.15
    
    return time, u_m, v_m, w_m, t_sos


def read_xbox_imu(fname):
    
    """
    This Python script reads data from a Crossbow NAV440 IMU file in binary format.
    The file contains measurements of angular rates and accelerations in three directions.
    Optionally, the file may also contain measurements of velocity, GPS position, temperature, and time of week.
    
    The data is stored in lists, with each list containing measurements for one direction.
    
    Usage: 
    Call the `read_xbox_imu` function, providing the filename of the IMU data file as an argument. 
    The function returns a tuple containing numpy arrays with the measurements in SI units and a datetime64 array with timestamps.
    
    Requirements: 
    - Python 3
    - NumPy
    
    Author: [Marcel du Plessis, marcel.du.plessis@gu.se]
    Date: [24 February 2023]
    
    Args:
        fname (string): The file name of the binary file containing the IMU data.

    Returns:
        time: An array of datetime64 objects representing the timestamp.
        x_rate: X-axis angular rate (in degrees per second).
        y_rate: Y-axis angular rate (in degrees per second).
        z_rate: Z-axis angular rate (in degrees per second).
        x_accl: X-axis acceleration (in g's).
        y_accl: Y-axis acceleration (in g's).
        z_accl: Z-axis acceleration (in g's).
        x_accl: X-axis acceleration (in g's).
        y_accl: Y-axis acceleration (in g's).
        z_accl: Z-axis acceleration (in g's).  
        roll_ang : roll angle (in degrees)
        pitch_ang: pitch angle (in degrees)
        yaw_ang  : yaw angle (in degrees)
    
    """

    # initialize empty lists to store data
    time_string = []
    
    x_rate = [] 
    y_rate = [] 
    z_rate = [] 
    
    x_accl = [] 
    y_accl = [] 
    z_accl = [] 
    
    roll_ang  = [] 
    pitch_ang = [] 
    yaw_ang   = [] 

    # open the file in binary mode
    with open(fname, "rb") as f:
        
        # specify the size of each chunk to read
        chunk_size = 59
        
        # read the first chunk
        chunk = f.read(chunk_size)
        
        # keep reading chunks until end of file
        while chunk:
            
            # read the next chunk
            chunk = f.read(chunk_size)
            
            # if chunk is empty, skip to next iteration
            if chunk == b'':   
                continue     
            
            # extract the time string from the chunk
            time_str = '20' + str(chunk)[2:4] + '-' + str(chunk)[4:6] + '-' + str(chunk)[6:8] + ' ' + str(chunk)[8:10] + ':' + str(chunk)[10:12] + ':' + str(chunk)[12:18],
            
            try:
                # convert the time string to a datetime object
                time = np.array(time_str, dtype='datetime64[ms]')
                
                # append the time string to the list
                time_string.append(time_str)
                
                # extract and convert the x, y, and z rates from the chunk
                x_rate.append(struct.unpack('!h', chunk[17:][11:13])[0] * (1260 / 2 ** 16))
                y_rate.append(struct.unpack('!h', chunk[17:][13:15])[0] * (1260 / 2 ** 16))
                z_rate.append(struct.unpack('!h', chunk[17:][15:17])[0] * (1260 / 2 ** 16))
                
                # extract and convert the x, y, and z accelerations from the chunk
                x_accl.append(struct.unpack('!h', chunk[17:][17:19])[0] * (20 / 2 ** 16))
                y_accl.append(struct.unpack('!h', chunk[17:][19:21])[0] * (20 / 2 ** 16))
                z_accl.append(struct.unpack('!h', chunk[17:][21:23])[0] * (20 / 2 ** 16))
                
                roll_ang .append(struct.unpack('!h', chunk[17:][5:7]) [0]*(360/2**16)   )
                pitch_ang.append(struct.unpack('!h', chunk[17:][7:9]) [0]*(360/2**16)   )
                yaw_ang  .append(struct.unpack('!h', chunk[17:][9:11])[0]*(360/2**16)   )              
            
            except:            
                continue
        
    # convert the time string list to a numpy array of datetime objects
    time = np.array(time_string, dtype='datetime64[ms]')
    
    # squeeze the time array to remove any extra dimensions
    time = np.squeeze(time)

    # convert the lists to numpy arrays
    x_rate = np.array(x_rate)
    y_rate = np.array(y_rate)
    z_rate = np.array(z_rate)

    x_accl = np.array(x_accl)
    y_accl = np.array(y_accl)
    z_accl = np.array(z_accl)
    
    roll_ang  = np.array(roll_ang )
    pitch_ang = np.array(pitch_ang)
    yaw_ang   = np.array(yaw_ang  )       
    
    # return the data as numpy arrays
    return time, x_rate, y_rate, z_rate, x_accl, y_accl, z_accl, roll_ang, pitch_ang, yaw_ang  



def read_gps(fname):
    """
    Reads data from a Hemisphere Crescent VS 100 GPS Compass and returns the time stamps, position status, latitude, longitude,
    speed over ground, course over ground, magnetic variation, and variation direction.
    
    Args:
        fname: A string representing the path to the file to read
    
    Returns:
        time_gps: GPS time stamps in the format of yyyy-mm-dd hh:mm:ss.ssssss
        time_moxa: time stamps of the Moxa device in the format of yyyy-mm-dd hh:mm:ss.ssssss
        pos_status: position status ('A' for data valid or 'V' for data invalid)
        latitude: latitude in decimal degrees
        longitude: longitude in decimal degrees
        sog_kts: speed over ground in knots
        cog: course over ground in degrees true
        mag_var: magnetic variation in degrees
        var_dir: variation direction ('E' for east or 'W' for west)
    """
    
    # Initialize lists for the data
    pos_status = []
    latitude   = []
    longitude  = []
    sog_kts    = []
    cog        = []
    mag_var    = []
    var_dir    = []
    time_gps   = [] 
    time_moxa  = []
    
    # Read the file into a DataFrame using Pandas
    gps = pd.read_csv(fname, sep='\t', header=None, names=['time', 'other'])

    # Determine the starting index based on the first data type
    if gps.iloc[0]['other'].split(",")[0]=='$GPRMC':
        start_idx = 0
        
    elif gps.iloc[0]['other'].split(",")[0]=='$GPVTG':
        start_idx = 1
    
    elif gps.iloc[0]['other'].split(",")[0]=='$GPHDT':
        start_idx = 2
    
    # Iterate through every third line starting from the starting index and extract the relevant data
    for i in range(gps.iloc[start_idx::3]['other'].size):
        
        try:
            # Extract the necessary data from the line using string manipulation
            GPRMC = gps.iloc[start_idx::3].iloc[i]['other'].split(",")        
            utc  = GPRMC[1]
            date = GPRMC[9]            
            lon, lat = mc.lonlat_convert(GPRMC[5], GPRMC[3]) # Call the lonlat_convert function to convert the longitude and latitude
            
            # Append the extracted data to the appropriate list
            pos_status.append(GPRMC[2])
            latitude  .append(lat)
            longitude .append(lon)            
            sog_kts   .append(GPRMC[7])
            cog       .append(GPRMC[8])    
            mag_var   .append(GPRMC[10])
            var_dir   .append(GPRMC[11])
            
            # Convert the GPS time and Moxa time to the appropriate format using the gps_time_convert and moxa_time_convert functions
            time_gps.append(mc.gps_time_convert(date, utc))
            tm = str(gps.iloc[start_idx::3].iloc[i]['time'])            
            time_moxa.append(mc.moxa_time_convert(tm))
            
        except:          
            continue 
            
    sog_kts    = np.array(sog_kts).astype(np.float64)
    latitude   = np.array(latitude).astype(np.float64)
    longitude  = np.array(longitude).astype(np.float64)
    cog        = np.array(cog).astype(np.float64)
    
    time_gps = pd.to_datetime(time_gps, format='%Y-%m-%d %H:%M:%S.%f')
    time_moxa = pd.to_datetime(time_moxa, format='%Y-%m-%d %H:%M:%S.%f')
    
    return time_gps, time_moxa, pos_status, latitude, longitude, sog_kts, cog, mag_var, var_dir
