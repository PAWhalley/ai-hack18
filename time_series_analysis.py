import pandas as pd
import numpy as np
import util

def histogram(data, feature=None, value=1, bin_size=60*60*24):
	df = util.remove_missing(data, "timestamp")

	if feature != None:
		value_array = value
		if not isinstance(value, list):
			value_array = [value]

		df = df[np.isin(df[feature], value)]

	df_values = df["timestamp"].values
	df_values = df_values[~np.isnan(df_values)]

	bins = np.arange(df_values.min(), df_values.max(), bin_size)

	hist, __ = np.histogram(df["timestamp"], bins=bins)


	x = (bins[:-1] + bins[1:]) / 2

	return x, hist

def stationary_mean(sequence):
	avg = np.average(sequence)

	return avg

def stationary_acvs(sequence, max_tau):
	mean = stationary_mean(sequence)
	s_tau = []

	for tau in range(max_tau):
		x_roll_tau = np.roll(sequence, tau)

		s_sum = np.sum(np.cross(sequence[tau:] - mean, x_roll_tau[tau] - mean))
		s_tau[tau] = s_sum / (sequence.size - tau)

	return s_tau