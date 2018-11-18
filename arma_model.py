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

	y = pd.read_csv('time_series.csv').values

	print(y)
	size = len(y)
	x = np.linspace(1,size, size).astype(int)

	mean = ts.stationary_mean(y)


	x_seasonal, freq, y_seasonal = ff.ffilt(x, y[:, 0], 4000, 10, 8)

	y_diff = y[8:-8, 0] - mean - y_seasonal.real

	return y_diff



arma_model = sm.tsa.ARMA(y, (7, 0), maxiter=500)
result = arma_model.fit()

print(arma_model.summary())
plt.plot(arma_model.resid)
pt.show()