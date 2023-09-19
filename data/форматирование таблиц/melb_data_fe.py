import pandas as pd
melb_data = pd.read_csv('форматирование таблиц/melb_data_fe.csv', sep = ',',header = None)
melb_data['Date'] = pd.to_datetime(melb_data['Date'])
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')

a = (melb_data.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc=['median'], fill_value = 0
)).max()
print(melb_data)


