from floodsystem.plot import plot_water_levels
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    at_risk=(stations_highest_rel_level(stations,5).name)
    for station in at_risk:
        plot_water_levels(station,fetch_measure_levels(station.id),fetch_measure_levels(station.id))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()