# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
#this function checks if the upper and lower bound on a given typical range, firstly both exits, then if they are both floats, if both requirements arent satisifed it returns false, else true.
def typical_range_consistent(self):
    if type(self.typical_range)!=tuple:
        return False
    else:
        if type((self.typical_range)[0])==float and type((self.typical_range)[1])==float:
            return True
        else:
            return False
#this function uses the function above and inserts any stations for which the value if false into a list which it later returns. 
def inconsistent_typical_range_stations(stations):
    faulty=[]
    for station in stations:
        if typical_range_consistent(station)==False:
            faulty.append(station.name)
    return faulty
#Task 2B
def relative_water_level(self):
    if typical_range_consistent(self)==False or self.latest_level==None:
        return None
    else:
        a=self.typical_range[0]
        b=self.typical_range[1]
        rel=self.latest_level/(b-a)-a/(b-a)
        return rel
