import pandas
import numpy as np
import sqlalchemy
import datetime


def sensor(number):
    sensor = "sensor_"
    for sensor in range (number + 1):
        print(sensor)


start_date = datetime.datetime.now() 
print(d)
end_date = start_date + datetime.timedelta(days=30)
print(de)

timestamp = 30 * 24 * 6

pandas.date_range(start=0, end=4320, freq='10min')