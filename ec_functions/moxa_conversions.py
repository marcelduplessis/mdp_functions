import numpy as np

def moxa_time_convert(time_str):
    """
    Converts a string representation of time in the format "YYMMDDHHmmss" 
    to the format "YYYY-MM-DD HH:MM:SS".
    
    Args:
    time_str (str): A string representation of time in the format "YYMMDDHHmmss".
    
    Returns:
    str: A string representation of time in the format "YYYY-MM-DD HH:MM:SS".
    """
    
    # Extract year, month, day, hour, minute, and second from the time string
    year = '20' + time_str[:2]
    month = time_str[2:4]
    day = time_str[4:6]
    hour = time_str[6:8]
    minute = time_str[8:10]
    second = time_str[10:]
    
    # Concatenate the extracted date and time elements to form the output string
    time_formatted = year + '-' + month + '-' +  day + ' ' + hour + ':' + minute + ':' + second
    
    return time_formatted




def lonlat_convert(ln, lt):
    """
    Converts longitude and latitude from degree-minute format to decimal degrees.

    Args:
    ln (str): longitude in degree-minute format (DDDMM.MMMM)
    lt (str): latitude in degree-minute format (DDMM.MMMM)

    Returns:
    lon (float): longitude in decimal degrees
    lat (float): latitude in decimal degrees
    """
    
    # Convert degrees and minutes to decimal degrees
    lon = np.array(ln[:3]).astype(np.float64) + np.array(ln[3:]).astype(np.float64)/60
    lat = np.array(lt[:2]).astype(np.float64) + np.array(lt[2:]).astype(np.float64)/60
    
    return lon, lat




def gps_time_convert(date, utc):
    """
    Convert GPS date and UTC time to a string of standard time format (YYYY-MM-DD HH:MM:SS).
    
    Args:
    - date: string, GPS date in the format of 'DDMMYY', where DD is the day, MM is the month, and YY is the year.
    - utc: string, UTC time in the format of 'HHMMSS.SSS', where HH is the hour, MM is the minute, and SS.SSS is the second with decimals.
    
    Returns:
    - time_str: string, a string of standard time format (YYYY-MM-DD HH:MM:SS).
    """
    
    # Extract hour, minute, and second from the UTC time
    hr = utc[:2] # hour
    mn = utc[2:4] # minutes
    sc = utc[4:] # seconds.seconds
    
    # Extract day, month, and year from the GPS date
    dy = date[:2] # day
    mt = date[2:4] # month
    yr = date[4:6] # year
 
    # Convert to the standard time format
    time_str = '20' + yr + '-' + mt + '-' + dy + ' ' + hr + ':' + mn + ':' + sc
    
    return time_str
