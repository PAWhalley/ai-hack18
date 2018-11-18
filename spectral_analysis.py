
import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_series_analysis as ts
import os
from scipy.fftpack import fft


#set the value of the bin
std_bin_size = 60*60*24

##get the data
#os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")
os.chdir("/Users/sotakao/Documents/GitHub/ai-hack18/")
data = util.read_with_timestamps("Road Accident/Road-Accident.csv")

##set path to folder for timestamps
#os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting

x, y = ts.histogram(data, "age_of_driver", value=36)


## computing the mean and reducing from the data to obtain mean zero new data
mean_y = ts.stationary_mean(y)
y_0 = y - mean_y
plt.plot(x, y_0)
plt.show()


## fourier transform
fy = fft(y_0)
fx = np.linspace(0.0, 300, 364)
plt.plot(fx, fy)
plt.show()

