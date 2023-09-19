import pandas as pd
rating_movies = pd.read_csv('объединение таблиц/ratings_movies.csv', sep = ',')
import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
rating_movies['year_release'] = rating_movies['title'].apply(get_year_release)
mask = rating_movies['year_release'] == 2018
grouped = rating_movies[mask].groupby('genres')['rating'].agg(
    ['mean', 'count']
)
a = grouped[grouped['count']>10].sort_values(
    by='mean',
    ascending=False
)
rating_movies['date'] = pd.to_datetime(rating_movies['date'])
rating_movies['year_rating'] = rating_movies['date'].dt.year
pivot = rating_movies.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)

print(pivot['2018'])
