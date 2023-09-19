import pandas as pd
citi_data = pd.read_csv('123\citibike-tripdata.csv', sep = ',')
citi_data = citi_data.drop(['start station id','end station id'], axis = 1)
citi_data['age'] = 2018-citi_data['birth year']
citi_data = citi_data.drop(['birth year'],axis=1)
citi_data['starttime'] = pd.to_datetime(citi_data['starttime'])
citi_data['stoptime'] = pd.to_datetime(citi_data['stoptime'])
citi_data['trip duration'] = citi_data['stoptime']-citi_data['starttime']
weekend = citi_data['starttime'].dt.dayofweek
citi_data['weekend'] = weekend.apply(lambda x: 1 if x == 5 or x == 6 else 0)
citi_data['weekend'].sum()
def time_of_day(time):
    if 0<=time<=6:
        return 'night'
    if 6<time<=12:
        return 'morning'
    if 12<time<=18:
        return 'day'
    if 18<time<=23:
        return 'evening'
citi_data['time_of_day'] = citi_data['starttime'].dt.hour.apply(time_of_day)
a = citi_data[citi_data['time_of_day'] == 'day'].shape[0]
b = citi_data[citi_data['time_of_day'] == 'night'].shape[0] 
print(round(a/b))