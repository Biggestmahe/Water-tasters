import numpy as np
import matplotlib.dates as mdates
def polyfit(dates, levels, p):
    dates= mdates.date2num(dates)
    a = dates[0]
    for i in range(len(dates)):
        dates[i] -= a
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    return (poly , a)


