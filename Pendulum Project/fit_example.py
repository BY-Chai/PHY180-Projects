# Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb
import math

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b

# Next, generate your data and errorbars.
# Note that xerr and yerr can either be an array of the same length as x&y, or a single value

# Let's try again, this time loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Polynomial fitting functions
def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

def cubic(t, a, b, c, d):
    return a*t**3 + b**t**2 + c*t + d

def quartic(t, a, b, c, d, e):
    return a*t**4 + b**t**3 + c*t**2 + d*t + e

def quintic(t, a, b, c, d, e, f):
    return a*t**5 + b*t**4 + c**t**3 + d*t**2 + e*t + f

# Exponential fitting function
def exponent(t, a, b):
    return a*math.e^(b*t)

# Power fitting function
def power(t, k, n):
    return k*t**n

# Now load the data from the file. The file should be in the same directory as this Python code.

filename="length-Q.txt"
x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

init_guess = (-200, -20, 56) # guess for the best fit parameters
font_size = 12
xlabel = "Wire Length (m)"
ylabel = "Q"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
best_guess = bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel)

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

print(best_guess[2])