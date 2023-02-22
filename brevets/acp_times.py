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
maxSpeed = {200km:34, 400km:32, 600km:30, 1000km:28, 1300km:26}
minSpeed = {60km:20, 600km:15, 1000km:11.428, 1300km:13.33}


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
    if control_dist_km == 0:
        return brevet_start_time
    for dist, time in maxEndTimes.values():
        if control_dist_km < dist:
            return_time = control_dist_km / time
            hours = int(str(return_time).split('.')[0]) # calculates hours by splitting fraction
            mins = int(float(str(return_time).split('.')[1]) * 60) # cacluates mins by multiplying float by 60
                                                                   # and then truncating
            # account for late start time
            if (dist==60km):
                hours+=1
        else:
            int_time = 
            return arrow.now # fix this with new hours/mins



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
        return brevet_start_time # + 1
    if control_dist_km >= brevet_dist_km:
        return endTimes(brevet_dist_km)
    return arrow.now()
