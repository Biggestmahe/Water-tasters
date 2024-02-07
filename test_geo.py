import floodsystem.geo
from floodsystem.stationdata import build_station_list
import floodsystem.station



def test_rns():
    #create list of fake stations
    station1= station.MonitoringStation(0,0,"station 1",(0,0),0,0,"river 1","town 1")
    station2= station.MonitoringStation(0,0,"station 2",(10,0),0,0,"river 1","town 2")
    station3= station.MonitoringStation(0,0,"station 3",(0,10),0,0,"river 2","town 3")
    stations=[station1,station2,station3]
    #manually computed result to compare to
    comparison = [('River 1',2)]
    calculated = geo.rivers_by_station_number(stations,1)
    if comparison==calculated:
        print("rivers by number of stations currently functional")
    else:
        print("rivers by number of stations failed.")


