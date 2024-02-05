from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    rivers = list(rivers_with_station(stations))
    rivers.sort()
    print(str(len(rivers)) + " stations. First 10: "+ str(rivers[:10]))

    river2 = stations_by_river(build_station_list())
    River_Aire= river2["River Aire"]
    River_Cam= river2["River Cam"]
    River_Thames= river2["River Thames"]
    print("River Aire: "+ River_Aire)
    print("River Cam"+ River_Cam)
    print("River Thames"+ River_Thames)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
