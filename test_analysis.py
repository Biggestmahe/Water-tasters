from floodsystem.analysis import polyfit 
import math
import datetime
def test_polyfit():
    dates = [datetime.datetime(2020, 5, 17), datetime.datetime(2020, 5, 18),datetime.datetime(2020, 5, 19),datetime.datetime(2020, 5, 20) ]
    levels=[0,1,2,3]
    function = polyfit(dates,levels, 1)
    assert function[0](10) == 10
    levels = [0,1,4,9]
    function = polyfit(dates,levels, 2)
    assert math.isclose(function[0](10),100, rel_tol=0.0001)
test_polyfit()
