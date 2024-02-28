# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    l= stations_highest_rel_level(10)
    final=[]
    for i in l:
        final.append(i.name)
    print(final)
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()