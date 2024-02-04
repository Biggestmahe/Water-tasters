# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
import numpy as np
from .utils import sorted_by_key  # noqa
#task 1B
def stations_by_distance(stations, p):
    statdist=[]
    for station in stations:
        distance=haversine(station.coord, p)
        statdist.append((station,distance))
        statdist=sorted_by_key(statdist,i=1)
    return statdist

#finding which stations are within radius r from a specific centre 
def stations_within_radius(stations, centre, r):
    within = []
    distances= stations_by_distance(stations, centre)
    for i in distances :
        
        if i[1] <= r :
            within.append(i[0])
    return within

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        if station.measure_id == None :
            pass
        else:
            rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    rivers = list(rivers_with_station(stations))
    station_river = {key: [] for key in rivers}
    for station in stations:
        station_river[station.river].append(station.name)
    return station_river

def rivers_by_station_number(stations, N):
    nstat=[]
    output=[]
    x=list(stations_by_river(stations).values())
    y=list(stations_by_river(stations).keys())
    for i in range(len(y)):
        nstat.append((y[i],len(x[i])))
    nstat=sorted_by_key(nstat,i=1,reverse=True)
    for j in range(N):
        output.append(nstat[j])
    while nstat[N-1][1]==nstat[N][1] and N<len(y)-1:
        output.append(nstat[N])
        N+=1
    return output