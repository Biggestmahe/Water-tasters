from floodsystem.stationdata import build_station_list
from floodsystem.station import typical_range_consistent
from floodsystem.station import inconsistent_typical_range_stations

#requirements for task 1F
def run():
    # Build list of stations
    stations = build_station_list()
    print("List of stations giving faulty data:")
    #print list of faulty stations
    print(inconsistent_typical_range_stations(stations))
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()