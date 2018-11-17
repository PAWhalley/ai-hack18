import pandas as pd
import numpy as np

def read_with_timestamps(path):
	data = pd.read_csv(path, sep=",")
	timestamps = pd.read_csv("timestamp.csv", sep=",")

	data.insert(0, "timestamp", timestamps)

	return data

def remove_missing(df, feature):
	missing = np.logical_and(np.isnan(df[feature]), np.less(df[feature], 0))

	df = df[np.logical_not(missing)]

	return df