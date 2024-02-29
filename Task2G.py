import datetime
import numpy as np
import matplotlib as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.Flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
update_water_levels(stations)
stationsover = stations_level_over_threshold(stations, 1)
#flooding risk hard to judge if just looking at how close level is to record high, using derivative (rate of increase of water level) as well
severe = set()
high = set()
moderate = set()
low = set()
for station in stationsover:
    (dates, levels) = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
    if dates == [] or levels == []:
        pass
    else:
        poly, d0 = polyfit(dates, levels, 4)
        derivative = np.polyder(poly, 1)
        value = derivative(plt.dates.date2num(dates[-1]) - d0)
        if station[0].town == None or value > 0 :
             pass
        elif station[1] > 1.7 :
            severe.add(station[0].town)
        elif station[1] > 1.4 :
            high.add(station[0].town)
        elif station[1] > 1.2 :
            moderate.add(station[0].town)
        else:
            low.add(station[0].town)

print("--STATIONS WITH SEVERE FLOOD RISK--")
print(severe)
print("--STATIONS WITH HIGH FLOOD RISK--")
print(high)
