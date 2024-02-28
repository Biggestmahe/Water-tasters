import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates, levels, p):
    p_coeff = np.polyfit(dates-dates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly , dates[0])


