from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from test_geo import test_rns
#requirements for task 1E

def run():
    # Build list of stations
    stations = build_station_list()
    #set number of rivers to be shown
    N=10
    #display data from first N rivers
    print("First " + str(N) + " rivers by number of stations. (inclusive)")

    print(rivers_by_station_number(stations, N))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
    test_rns()