import pandas as pd
import numpy as np

def correlation(feature1, feature2, data):
	df = pd.DataFrame(data, columns=[feature1, feature2])

	missing1 = np.logical_and(np.isnan(df[feature1]), np.less(df[feature1], 0))
	missing2 = np.logical_and(np.isnan(df[feature1]), np.less(df[feature2], 0))

	df = df[np.logical_not(np.logical_or(missing1, missing2))]

	correlation = df.corr()

	return correlation

def class_correlation(feature1, feature2, data):
	df = pd.DataFrame(data, columns=[feature1, feature2])

	missing1 = np.logical_and(np.isnan(df[feature1]), np.less(df[feature1], 0))
	missing2 = np.logical_and(np.isnan(df[feature1]), np.less(df[feature2], 0))

	df = df[np.logical_not(np.logical_or(missing1, missing2))]
	df = pd.get_dummies(df, columns=[feature1, feature2])

	correlation = df.corr()

	return correlation