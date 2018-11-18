import pandas as pd
import numpy as np

def read_with_timestamps(path):
	data = pd.read_csv(path, sep=",", low_memory=False)
	timestamps = pd.read_csv("timestamps.csv", sep=",", low_memory=False)

	data.insert(0, "timestamp", timestamps)

	return data

def remove_missing(df, feature):
	df = df[np.logical_not(np.isnan(df[feature]))]
	df = df[np.logical_not(np.less(df[feature], 0))]

	return df