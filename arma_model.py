import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import matplotlib.pyplot as plt
import util
import fourier_filtering as ff
import time_series_analysis as ts
import pandas as pd

def prepare():
	data = util.read_with_timestamps("/Users/TylerFarghly/Documents/Projects/ai-hack18/ai-hack18/Road Accident/Road-Accident.csv")

	y = pd.read_csv('time_series.csv').values[:, 0]

	print(y)
	size = len(y)
	x = np.linspace(1,size, size).astype(int)

	mean = ts.stationary_mean(y)
	print(mean)

	x_seasonal, freq, y_seasonal = ff.ffilt(x, y, 2000, 10, 8)


	y_diff = y[8:-8] - mean - y_seasonal.real
	plt.plot(y[8:-8])
	plt.plot(y_diff + mean)
	plt.show()

	plt.figure()
	plt.plot(y_diff)
	plt.show()

	return y_diff