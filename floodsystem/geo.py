# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def stations_within_radius(stations, centre, r):
    within = []
    for station in stations :
        if ((station.coord[0] - centre[0])**2 + (station.coord[1] - centre[1])**2 ) <= r :
            within.append(station)
    return within