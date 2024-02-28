import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from .analysis import polyfit
def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels)
    lower,upper=[],[]
    for i in range(len(dates)):
        lower.append(station.typical_range[0])
        upper.append(station.typical_range[1])
    plt.plot(dates,upper)
    plt.plot(dates,lower)
    plt.xlabel("time")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, levels, '.')
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))    
    plt.show()