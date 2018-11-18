import numpy as np
import matplotlib.pyplot as plt
import time_series_analysis as ts

def ffilt(timestamp,time_series,amp_threshold,freq_threshold,snip_ends=0):
	mean_ts = ts.stationary_mean(time_series)
	y = time_series - mean_ts
	y = y[snip_ends:-snip_ends]
	x = timestamp
	fy = np.fft.fft(y)
	old_fy = fy
	freq = np.fft.fftfreq(len(y), 1)
	fy_abs = np.abs(fy)

	# Truncate frequency greater than freq_threshold
	# with amplitude less than amp_threshold
	for i in range(fy.shape[0]):
		if fy_abs[i] < amp_threshold or abs(freq[i]) > freq_threshold:
			fy[i] = 0


	# Take inverse Fourier transform
	ffy = np.fft.ifft(fy)

	# Plot figures
	fig1 = plt.figure()
	plt.plot(freq,old_fy,'k')
	plt.plot(freq,fy,'r')

	plt.title("Frequency plot")
	fig2 = plt.figure()
	plt.plot(x[snip_ends:-snip_ends], y,'k')
	plt.plot(x[snip_ends:-snip_ends],ffy,'r')
	plt.title("Filtered time series")
	plt.show()

	# # Dominant frequency

	# dom = max(np.abs(fy))

	# return dom


