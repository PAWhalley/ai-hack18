
import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_histogram as th
import os

#set the value of the bin
std_bin_size = 60*60*24

##get the data
#os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")
os.chdir("/Users/sotakao/Documents/GitHub/ai-hack18/")
data = util.read_with_timestamps("Road Accident/Road-Accident.csv")

##set path to folder for timestamps
#os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting
print(type(data))
x,y,z = th.time_histogram("age_of_driver", data, value=24)

# obtain Fourier transform

# Interpolate values for x and y.
t = np.linspace(0, 1, len(x))
t2 = np.linspace(0, 1, 2*len(x))
# One-dimensional linear interpolation.
x2 = np.interp(t2, t, x)
y2 = np.interp(t2, t, y)

fig1 = plt.figure()
plt.scatter(x,y,marker='o', color='k')
plt.scatter(x2,y2,marker='o', color='r')
plt.show()

y2 = y2 - ts.stationary_mean(y2)
size = np.arange(len(y2))
fy = np.fft.fft(y2)
freq = np.fft.fftfreq(size.shape[-1])

fig2 = plt.figure()
plt.plot(fy)
plt.show()