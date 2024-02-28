import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels)
    plt.xlabel("time")
    plt.ylabel("Water Level (m)")
    plt.title(station.name)

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, levels, '.')
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))    
    plt.show()