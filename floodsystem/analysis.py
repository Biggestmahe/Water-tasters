import numpy as np
import matplotlib.dates as mdates
def polyfit(dates, levels, p):
    date= mdates.date2num(dates)
    a = date[0]
    for i in range(len(date)):
        date[i] -= a
    p_coeff = np.polyfit(date, levels, p)
    poly = np.poly1d(p_coeff)
    return (poly , a)


