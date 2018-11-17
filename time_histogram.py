import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import util

def time_histogram(feature, data, value=1, bin_size=60*60*24):
	df = util.remove_missing(data, "timestamp")
	df_feature = df[np.equal(df[feature], value)]

	df_values = df["timestamp"].values
	df_values = df_values[~np.isnan(df_values)]

	bins = np.arange(df_values.min(), df_values.max(), bin_size)

	hist, bins1 = np.histogram(df["timestamp"], bins=bins)
	hist_feature, bins2 = np.histogram(df_feature["timestamp"], bins=bins)


	x = bins[1:]

	return x, hist_feature, hist