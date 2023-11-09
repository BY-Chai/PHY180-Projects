import fit_DHM as DHM

def truncate(xdata, ydata, xerr, yerr, angle_fraction):
    end_angle = angle_fraction * max(ydata)
    i = ydata.where(end_angle)[0]
    return xdata[:i], ydata[:i], xerr[:i], yerr[:i]

DHM.peak_picker()