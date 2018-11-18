import pandas
import numpy as np
import matplotlib.pyplot as plt
import util
import time_series_analysis as ts
import os
from scipy.fftpack import fft


#set the value of the bin
std_bin_size = 60*60*24

##get the data
os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")
data = util.read_with_timestamps("Road-Accident.csv")

##set path to folder for timestamps
os.chdir(r"C:\Users\REMY\Documents\GitHub\ai-hack18")

## plotting the simple moving average
def calcSma(data, smaPeriod):
    j = next(i for i, x in enumerate(data) if x is not None)
    our_range = range(len(data))[j + smaPeriod - 1:]
    empty_list = [None] * (j + smaPeriod - 1)
    sub_result = [np.mean(data[i - smaPeriod + 1: i + 1]) for i in our_range]

    return np.array(empty_list + sub_result)

x, y = ts.histogram(data, "age_of_driver", value=25)
CMAweekly, CMAmonthly = calcSma(y, 7), calcSma(y, 30)

#plt.plot(x, CMAweekly)
#plt.plot(x, CMAmonthly)
#plt.show()

## constructing data ("day", "number of accident during the day")
DayShift = 16436
#16 436 is the number of days between 1st jan 1970 and 1st jan 2015, which is the year of the data

def daily_data(x = data, DayShift = 16436):
    new_data = []
    for index in x:
        new_value = (int( (int(index) - DayShift * 3600 * 24)) - int(( (int(index) - DayShift * 3600 * 24) % (3600 * 24) ) ) /3600 / 24)
        new_data.append(new_value)
    return new_data

def remove_monthly():
    cleaned_data = []
    for i in range(len(CMAmonthly)):
        if CMAweekly[i] is None or CMAmonthly[i] is None:
            cleaned_data.append(None)
        else:
            new_value = CMAweekly[i] - CMAmonthly[i]
            cleaned_data.append(new_value)
    return cleaned_data

new_data = remove_monthly()

print(len(new_data), print(new_data))


##Plotting weekly and monthly CMAs

os.chdir(r"C:\Users\REMY\Documents\5. Coding\Hackatons\2018 AI Hack\Data\Road Accident")

fig = plt.figure()
plt.plot(x, y)
plt.title("CMA")
plt.xlabel('Time [s]')
plt.ylabel('Casualties')




fig1 = plt.figure()
plt.plot(x, CMAweekly)
plt.title("Weekly CMA")
plt.xlabel('Time [s]')
plt.ylabel('Casualties')

fig2 = plt.figure()
plt.plot(x, CMAmonthly)
plt.title("Monthly CMA")
plt.xlabel('Time [s]')
plt.ylabel('Casualties')
#fig.plt.show()


