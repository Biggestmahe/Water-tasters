import floodsystem.geo
from floodsystem.stationdata import build_station_list
import floodsystem.station

def test_station_by_distance():
    station1= station.MonitoringStation(0,0,"station 1",(0,0),(0,0),"river 1","town 1")
    station2= station.MonitoringStation(0,0,"station 2",(10,0),(0,0),"river 2","town 2")
    station3= station.MonitoringStation(0,0,"station 3",(0,10),(0,0),"river 3","town 3")
    distance = geo.stations_by_distance([station1,station2,station3],(0,0))
    output = []
    for i in distance:
        output.append((i[0].name , i[0].town , i[1]))
    assert output == [('station 1', 'town 1', 0.0), ('station 2', 'town 2', 1111.950802335329), ('station 3', 'town 3', 1111.950802335329)]

def test_stations_within_radius():
    station1= station.MonitoringStation(0,0,"station 1",(0,0),(0,0),"river 1","town 1")
    station2= station.MonitoringStation(0,0,"station 2",(10,0),(0,0),"river 2","town 2")
    station3= station.MonitoringStation(0,0,"station 3",(0,10),(0,0),"river 3","town 3") 
    #finding station in distance of 1 kiloometers from (0,0)  
    stations_within_1=geo.stations_within_radius([station1,station2,station3],(0,0),1)
    output = []
    for i in stations_within_1 :
        output.append(i.name)
    assert output == ['station 1']
    #finding station in distance of 10000 kiloometers from (0,0)  
    stations_within_1=geo.stations_within_radius([station1,station2,station3],(0,0),10000)
    output = []
    for i in stations_within_1 :
        output.append(i.name)
    assert output == ['station 1','station 2','station 3' ]

def test_rivers_with_station():
    station1= station.MonitoringStation(0,0,"station 1",(0,0),(0,0),"river 1","town 1")
    station2= station.MonitoringStation(0,0,"station 2",(10,0),(0,0),"river 2","town 2")
    station3= station.MonitoringStation(0,0,"station 3",(0,10),(0,0),"river 2","town 3") 
    rivers= geo.rivers_with_station([station1,station2,station3])  
    assert rivers == {"river 1", "river 2"}

def test_stations_by_river():
    station1= station.MonitoringStation(0,0,"station 1",(0,0),(0,0),"river 1","town 1")
    station2= station.MonitoringStation(0,0,"station 2",(10,0),(0,0),"river 2","town 2")
    station3= station.MonitoringStation(0,0,"station 3",(0,10),(0,0),"river 2","town 3")    
    station4= station.MonitoringStation(0,0,"station 4",(0,10),(0,0),"river 3","town 3")
    station_river= geo.stations_by_river([station1,station2,station3, station4])
    assert station_river == {"river 1":["station 1"], "river 2":["station 2", "station 3"] , "river 3":["station 4"]}


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


test_station_by_distance()
test_stations_within_radius()
test_rivers_with_station()
test_stations_by_river()
