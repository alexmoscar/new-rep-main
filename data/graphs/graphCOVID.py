import pandas as pd
import matplotlib.pyplot as plt
covid_data = pd.read_csv('graphs/covid_data.csv')
vaccine = pd.read_csv('graphs/country_vaccinations.csv')
vaccine = vaccine[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]
covid_data = covid_data.groupby(['date','country'],as_index = False)[['confirmed','deaths','recovered']].sum()
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data['active'] = covid_data['confirmed']-covid_data['deaths']-covid_data['recovered']
covid_data = covid_data.sort_values(by=['country','date'])
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()
vaccine['date'] = pd.to_datetime(vaccine['date'])
covid_df = covid_data.merge(vaccine,on = ['date','country'], how = 'left')




