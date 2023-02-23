"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


#speed dicts
maxSpeed = {200:34, 400:32, 600:30, 1000:28, 1300:26}
minSpeed = {60:20, 600:15, 1000:11.428, 1300:13.33}

brevetEndTimes = {200:13.5, 300:20, 400:27, 600:40, 1000:75, 1200:90, 1400:116.4, 2200:220}

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    hours = 0
    mins = 0
    prev_dist = 0
    if control_dist_km == 0:
        return brevet_start_time
    for dist, time in maxSpeed.items():
        if control_dist_km < dist:
            return_time = (control_dist_km - prev_dist) / time
            hours += int(return_time)
            mins_tmp = return_time - int(return_time)
            mins += int(mins_tmp * 60)
            #hours = int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
            #mins = int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
                                                                   # and then truncating
            brevet_start_time.shift(hours=hours, minutes=mins)
            return brevet_start_time
        else:
            return_time = (control_dist_km - prev_dist) / time
            hours += int(return_time)
            mins_tmp = return_time - int(return_time)
            mins += int(mins_tmp * 60)
            #hours += int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
            #mins += int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
                                                                   # and then truncating
            brevet_start_time.shift(hours=hours, minutes=mins)
            prev_dist = dist #update prev_dist for next dist calc



    return arrow.now()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=+1)
    # if control is greater than final brevet dist, we need to just return final brevet calc
    if control_dist_km >= brevet_dist_km:
        return_time = brevetEndTimes(brevet_dist_km)
        hours = int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
        mins = int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
        return brevet_start_time.shift(hours = hours, minutes=mins) 
    for dist, time in minSpeed.items():
        if control_dist_km < dist:
            return_time = (control_dist_km - prev_dist) / time
            hours = int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
            mins = int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
                                                                   # and then truncating
            brevet_start_time.shift(hours = hours, minutes=mins)
            # account for late start time
            if (control_dist_km < 60):
                brevet_start_time.shift(hours=+1)
            return brevet_start_time
        else:
            return_time =  (control_dist_km - prev_dist) / time
            hours += int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
            mins += int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
                                                                   # and then truncating
            brevet_start_time.shift(hours=hours, minutes=mins)
            prev_dist = dist #update prev_dist for next dist calc
            return brevet_start_time

    return arrow.now()
