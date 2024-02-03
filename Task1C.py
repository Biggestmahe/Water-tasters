from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

near_stations=stations_within_radius(build_station_list(),(52.2053, 0.1218), 10)
output = []
for i in near_stations:
    output.append(i.name)
output.sort()
print(output)
