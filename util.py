import pandas as pd

def read_with_timestamps(path):
	data = pd.read_csv(path, sep=",")
	timestamps = pd.read_csv("timestamps.csv", sep=",")

	print(timestamps)

	data.insert(0, "timestamps", timestamps)

	return data