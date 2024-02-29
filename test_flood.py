from floodsystem.station import MonitoringStation
import floodsystem.geo
from floodsystem.Flood import stations_level_over_threshold
def test_statoverthresh():
    station1= MonitoringStation(0,0,"station 1",(0,0),(1.2,2.2),"river 1","town 1")
    station2= MonitoringStation(0,0,"station 2",(10,0),(None,0),"river 1","town 2")
    station1.latest_level=2.2
    assert stations_level_over_threshold([station1,station2],0.8)==[(station1, 1.0)]
    station1.latest_level=1.2
    assert stations_level_over_threshold([station1,station2],0.8)==[]
test_statoverthresh()