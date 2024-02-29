from floodsystem.plot import plot_water_level_with_fit
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    at_risk=stations_highest_rel_level(stations,1)
 
    for station in at_risk:
        plot_water_level_with_fit (station,  fetch_measure_levels(station.measure_id,datetime.timedelta(days=2))[0],  fetch_measure_levels(station.measure_id,datetime.timedelta(days=2))[1],4 )
if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()