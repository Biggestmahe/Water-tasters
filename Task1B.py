import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

lis=geo.stations_by_distance(build_station_list(),(52.2053, 0.1218))[:10]
output = []
for i in lis:
    output.append((i[0].name , i[0].town , i[1]))
print(output)
