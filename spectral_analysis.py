
import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_series_analysis as ts
import pandas as pd
import os
from scipy.fftpack import fft


pete_data = pd.read_csv("AverageData.csv")

#set the value of the bin
std_bin_size = 60*60*24

##get the data
#os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")
os.chdir("/Users/sotakao/Documents/GitHub/ai-hack18/")
data = util.read_with_timestamps("Road Accident/Road-Accident.csv")

##set path to folder for timestamps
#os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting

x, y = ts.histogram(data)

y = y[8:-8]

mean_y = ts.stationary_mean(y)
y_0 = y - mean_y


## fourier transform
fy = np.fft.fft(y_0)
freq = np.fft.fftfreq(len(y_0), 1)
#fx = np.linspace(0.0, 300, 364)
fy_abs = np.abs(fy)

plt.plot(freq, np.abs(fy))
plt.show()

for i in range(fy.shape[0]):
	if fy_abs[i] < 1000 or abs(freq[i]) > 0.03:
		fy[i] = 0

plt.figure()
plt.plot(freq, np.abs(fy))
plt.show()

ffy = np.fft.ifft(fy)
fy2 = y-ffy

fig = plt.figure()
plt.plot(x[8:-8], y_0,'k')
plt.plot(x[8:-8],ffy,'r')
print(pete_data.values[0,:])
plt.plot(x[9:-9], pete_data.values[0,:] - mean_y)
plt.show()

fig = plt.figure()
plt.plot(x[8:-8],fy2,'k')
plt.show()





