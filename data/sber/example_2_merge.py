import pandas as pd

data1 = {'human':['man', 'woman', 'man', 'man', 
                 'woman', 'man', 'woman', 'man', 'man'],
        'height':[178, 165, 190, 174, 160, 156, 170, 182, 170]}

data2 = {'human':['man', 'woman', 'man', 'man', 
                 'woman', 'man', 'woman', 'man', 'man'],
        'weight':[70, 60, 90, 67, 58, 75, 65, 80, 65]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df = df1.merge(df2, on='human', how='left')

print(df)