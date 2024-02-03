from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

rivers = list(rivers_with_station(build_station_list()))
rivers.sort()
print(str(len(rivers)) + " stations. First 10: "+ str(rivers[:10]))

river2 = stations_by_river(build_station_list())
River_Aire= river2["River Aire"]
River_Cam= river2["River Cam"]
River_Thames= river2["River Thames"]
print(River_Aire)
print(River_Cam)
print(River_Thames)
