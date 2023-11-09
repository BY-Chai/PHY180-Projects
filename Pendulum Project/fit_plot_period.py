### Takes in time-angle raw data from Tracker ###

import fit_black_box as bb
import math
import numpy as np

'''def truncate(xdata, ydata, xerr, yerr, angle_fraction):
    end_angle = angle_fraction * max(ydata)
    i = ydata.where(end_angle)[0]
    return xdata[:i], ydata[:i], xerr[:i], yerr[:i]'''

# Finds peaks of data by comparing with neighbour points
def peak_picker(xdata, ydata, xerr, yerr):
    xpeaks = []
    ypeaks = []
    xpeakserr = []
    ypeakserr = []

    for i in range(len(ydata) - 1):
        if abs(ydata[i]) >= abs(ydata[i+1]) and abs(ydata[i]) >= abs(ydata[i-1]):
            xpeaks.append(xdata[i])
            ypeaks.append(ydata[i])
            xpeakserr.append(xerr[i])
            ypeakserr.append(yerr[i])
    return np.array(xpeaks), np.array(ypeaks), np.array(xpeakserr), np.array(ypeakserr)

def differences(xdata):
    points = []
    differences = []
    for i in range(1, len(xdata) - 1):
        points.append(xdata[i])
        differences.append(abs(xdata[i]-xdata[i-1]))
    return np.array(points), np.array(differences)

# xdata, ydata, xerr, yerr = peak_picker(xdata, ydata, xerr, yerr) # Only needed if plotting peaks

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

def exponent(t, a, b):
    return a*math.e^(b*t)

filename="60deg_long (48).txt"
xdata, ydata, xerr, yerr = bb.load_data(filename)
xdata, ydata, xerr, yerr = peak_picker(xdata, np.abs(ydata), xerr, yerr)
xdata, xdatadiff = differences(xdata)

import matplotlib.pyplot as plt


plt.plot(xdata, xdatadiff)
plt.show()
