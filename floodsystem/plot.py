import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels)
    plt.xlabel("time")
    plt.ylabel("Water Level (m)")
    plt.title(station.name)
    plt.tight_layout()  

    plt.show()