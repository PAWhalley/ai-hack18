import ld
import time_series_analysis as tsa
import matplotlib.pyplot as plt
import numpy as np

data = ld.load()

x, y = tsa.histogram(data, bin_size=60*60)

acvs = tsa.stationary_acvs(y, 365)
zeros = np.zeros(acvs.shape[0])

plt.plot(acvs)
plt.plot(zeros)

plt.figure()
x = x - min(x)
x = x / 60 / 60
plt.plot(x, y)


plt.figure()
y_roll = np.roll(y, 24*7*4)
y_diff = y - y_roll
plt.plot(x, y_diff)

plt.show()