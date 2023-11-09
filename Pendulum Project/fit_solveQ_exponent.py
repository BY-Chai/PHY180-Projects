### Takes in time-angle raw data from Tracker ###

import fit_black_box as bb
import math
import numpy as np

def truncate(xdata, ydata, xerr, yerr, angle_fraction):
    end_angle = angle_fraction * max(ydata)
    for i in range(len(ydata)):
        if abs(ydata[i]) <= end_angle:
            break
    return xdata[:i], ydata[:i], xerr[:i], yerr[:i]

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

# xdata, ydata, xerr, yerr = peak_picker(xdata, ydata, xerr, yerr) # Only needed if plotting peaks

def linear(t, m, b):
    return m*t + b

# Defines an exponential function with base e for plot_fit
def exponent(t, a, b):
    return a*math.e**(-t/b)

filename="45deg_long.txt"
xdata, ydata, xerr, yerr = bb.load_data(filename)
xdata, ydata, xerr, yerr = peak_picker(xdata, ydata, xerr, yerr)
# xdata, ydata, xerr, yerr = truncate(xdata, ydata, xerr, yerr, 0.46)

# Using plot_fit
init_guess_exp = (0.8, 45) # exponent
font_size = 12
xlabel = "Time (s)"
ylabel = "Max Amplitude (rad)"


best_guess = bb.plot_fit(exponent, xdata, np.abs(np.radians(ydata)), xerr, yerr, init_guess=init_guess_exp, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel)

xdata, ydata, xerr, yerr = truncate(xdata, ydata, xerr, yerr, 0.53)
print("Manual Q:", len(ydata)/2 * 5)
# Why is this outputting larger Q values than manually counted