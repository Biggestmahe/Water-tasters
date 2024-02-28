import numpy as np
import matplotlib as plt
def polyfit(dates, levels, p):
    date= plt.dates.date2num(dates)
    a = date[0]
    for i in range(len(date)):
        date[i] -= a
    p_coeff = np.polyfit(date, levels, p)
    poly = np.poly1d(p_coeff)
    return (poly , a)


