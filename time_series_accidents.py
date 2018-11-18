import pandas as pd
import os
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import util
import numpy as np


x = np.linspace(0,364,365).astype(int)
data = util.read_with_timestamps("Road Accident/Road-Accident.csv")
bindata = np.zeros(366)
timestamp = data['timestamp']
timestamp = np.array(timestamp)
timestamp = (timestamp - min(timestamp))/(60*60*24)
for i in range(len(timestamp)-1):
	if timestamp[i] == timestamp[i+1]:
		None
	else:
		for j in x:
			if j<timestamp[i]<=j+1:
				bindata[j+1] = bindata[j+1]+1
	if i%10000 ==0:
		print("Done: "+str(i))

np.savetxt('time_series.csv',bindata,delimiter=',')
plt.figure()
plt.plot(bindata)
plt.show()
