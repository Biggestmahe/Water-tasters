# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

import floodsystem.geo
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation
def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_range():
    #create list of fake stations
    station1= MonitoringStation(0,0,"station 1",(0,0),(1.2,2.2),"river 1","town 1")
    station2= MonitoringStation(0,0,"station 2",(10,0),(None,0),"river 1","town 2")
    station3= MonitoringStation(0,0,"station 3",(0,10),(0,None),"river 2","town 3")
    stations=[station1,station2,station3]
    #manually computed result to compare to
    comparison = ['station 2','station 3']
    calculated = inconsistent_typical_range_stations(stations)
    assert comparison==calculated

    
test_range()