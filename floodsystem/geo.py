# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


#finding which stations are within radius r from a specific centre 
def stations_within_radius(stations, centre, r):
    within = []
    for station in stations :
        #this if statement check the distance
        if ((station.coord[0] - centre[0])**2 + (station.coord[1] - centre[1])**2 ) <= r**2 :
            within.append(station)
    return within