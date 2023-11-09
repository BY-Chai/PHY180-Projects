### Takes in time-angle raw data from Tracker ###

import fit_black_box as bb
import math
import numpy as np

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

# Defines an exponential function with base e for plot_fit
def exponent(t, a, b):
    return a*math.e**(-t/b)

# Defines the function representing damped harmonic motion for plot_fit
def harmonic(t, a, b, per, d):
    return a*np.exp(-t/b)*np.cos(2*np.pi*(t/per) + d)



filename="40deg_long (30).txt"
xdata, ydata, xerr, yerr = bb.load_data(filename)
# xdata, ydata, xerr, yerr = truncate(xdata, ydata, xerr, yerr, 0.46)

# Using plot_fit
init_guess = (0.26, 60, 1.03, 0) # harmonic
font_size = 12
xlabel = "Time (s)"
ylabel = "Amplitude (rad)"


best_guess = bb.plot_fit(harmonic, xdata, np.radians(ydata), xerr, yerr, init_guess=init_guess, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel)

per = best_guess[0][2]
b = best_guess[0][1]
q = math.pi * (b/per)
print("DHM:", q)