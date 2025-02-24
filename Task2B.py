from floodsystem.Flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol=0.8
    print(stations_level_over_threshold(stations,tol))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()