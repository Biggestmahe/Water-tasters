
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo



def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    closest=geo.stations_by_distance(stations,(52.2053, 0.1218))[:10]
    furthest= geo.stations_by_distance(stations,(52.2053, 0.1218))[10:]
    furthest.reverse()
    output = []
    for i in closest:
        output.append((i[0].name , i[0].town , i[1]))
    print("Closests are: "+ str(output))
    output = []
    for i in furthest:
        output.append((i[0].name , i[0].town , i[1]))
    print("Furthests are "+ str(output))



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
