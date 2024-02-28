from floodsystem.plot import plot_water_levels
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    at_risk=(stations_highest_rel_level(stations,5).name)
    for station in at_risk:
        plot_water_levels(station,fetch_measure_levels(station.id,10)[0],fetch_measure_levels(station.id,10)[1])

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()