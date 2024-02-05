# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    #using the function
    near_stations=stations_within_radius(stations,(52.2053, 0.1218), 10)
    output = []
    for i in near_stations:
        output.append(i.name)
    output.sort()
    print(output)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
