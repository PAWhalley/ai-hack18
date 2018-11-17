import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
import numpy as np
import math


data = pd.read_csv("/Users/peterwhalley/AIHACK2018//Road-Accident.csv", sep=",", low_memory=False)

def isnan(v):
    if not v < 0 and not v >= 0:
        return True
    else:
        return False

timedate = data["date"].values
timstr = data["time"].values

timestamp = np.zeros(timedate.shape[0])

#timstr= [x for x in timstr if (str(x) != "nan")]
#timstr = [x for x in timstr if type(x) != float]
for s in range(timedate.shape[0]):
    if len(timedate[s]) > 9:
        #timestamp[s] = float('NaN')
        timestamp[s] = time.mktime(time.strptime(timedate[s], '%d/%m/%Y'))
    else:
        timestamp[s] = (int(timedate[s]) - (25569))*24*60*60

    if (s%10000==0):
        print(s)

for s in range(timstr.shape[0]):
    if type(timstr[s]) == type("f"):
        x = time.strptime(timstr[s].split(" ")[1], "%H:%M:%S")
        timestamp[s] += datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    else:
        timestamp[s] = float('NaN')

    if (s%10000==0):
        print(s)
print(timestamp)
np.savetxt("25567.csv", timestamp, delimiter=",")
