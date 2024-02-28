from station import relative_water_level
from .utils import sorted_by_key
import statindata

def stations_level_over_threshold(stations, tol):
    x=list()
    for station in stations:
        if relative_water_level(station)!=None:
            if relative_water_level(station)>=tol:
                x.append(tuple(station,relative_water_level(station)))
    sorted_by_key(x,1,True)
    return x

import statindata

def stations_highest_rel_level(stations, N):
    touples= stations_level_over_threshold(stations, 0)[:N]
    station_list= []
    for i in touples:
        station_list.append(i[0])
    return station_list