# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key  # noqa
#task 1B
def stations_by_distance(stations, p):
    statdist=[]
    for station in stations:
        distance=2*6370*np.arcsin(np.sqrt(np.sin((station.coordinate[0]-p[0])/2)**2+np.cos(station.coordinate[0])+np.cos(p[0])*np.sin(station.coordinate[1]-p[1])/2))
        statdist.append(distance)
        print(statdist)

#finding which stations are within radius r from a specific centre 
def stations_within_radius(stations, centre, r):
    within = []
    for station in stations :
        #this if statement check the distance
        if ((station.coord[0] - centre[0])**2 + (station.coord[1] - centre[1])**2 ) <= r**2 :
            within.append(station)
    return within
