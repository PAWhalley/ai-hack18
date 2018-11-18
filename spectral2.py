
import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_series_analysis as ts
import pandas as pd
import os
from scipy.fftpack import fft

##set path to folder for timestamps
#os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting

y = pd.read_csv('time_series.csv').values[:,0]
x = np.linspace(1,len(y),len(y))

y = y[8:-8]

mean_y = ts.stationary_mean(y)
y_0 = y - mean_y


## fourier transform
fy = np.fft.fft(y_0)
old_fy = fy
freq = np.fft.fftfreq(len(y_0), 1)
#fx = np.linspace(0.0, 300, 364)
fy_abs = np.abs(fy)

mmax = 0
for i in range(len(fy)):
	if fy[i]>=mmax:
		mmax = fy[i]
		l=i

dom_freq = freq[l]


for i in range(fy.shape[0]):
	if fy_abs[i] < 2000 or abs(freq[i]) > 10:
		fy[i] = 0

fig1 = plt.figure()
plt.plot(freq[0:174], np.abs(fy)[0:174])
plt.title('Frequency plot of accidents per day')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
fig1.savefig('freqplot2.png')
plt.show()

ffy = np.fft.ifft(fy)
fy2 = y-ffy

fig2 = plt.figure()
plt.plot(x[8:-8], y_0,'k',label='Unfiltered time series')
plt.plot(x[8:-8],ffy,'r',label ='Filtered time series (monthly)')
plt.title('Seasonal trend of time series')
plt.xlabel('Time')
plt.ylabel('Number of accidents/day')
plt.legend()
fig2.savefig('filteredplot2.png')
plt.show()






