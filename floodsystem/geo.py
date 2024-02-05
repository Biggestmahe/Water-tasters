# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
import numpy as np
from .utils import sorted_by_key  # noqa

#task 1B finding the distances between every station and a coordinate this can be done by using the in built
#function of haversine. The inputs is the stations(MonitoringStation) and coordinate of p (float, float) and 
#the output is a list of (MonitoringStation, float)
def stations_by_distance(stations, p):
    statdist=[]
    for station in stations:
        distance=haversine(station.coord, p)
        statdist.append((station,distance))
        statdist=sorted_by_key(statdist,i=1)
    return statdist

#finding which stations are within radius r from a specific centre. the stations_by_distance has been used 
#to find all the distances and then got filter to which is less than input r. inputs are stations(MonitoringStation), 
# centre(float,float) and r(float) and the output is a list of stations(MonitoringStation).
def stations_within_radius(stations, centre, r):
    within = []
    distances= stations_by_distance(stations, centre)
    for i in distances :
        
        if i[1] <= r :
            within.append(i[0])
    return within

# This function represents the rivers which there has been atleast ono station in them, the output is a set which
#helps to do not recount any river if two or more station pass it
def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        if station.measure_id == None :
            pass
        else:
            rivers.add(station.river)
    return rivers

#this function uses rivers_with_station and as a dictionary gives us which stations passes through any river(key)
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
