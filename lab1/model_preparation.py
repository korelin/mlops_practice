import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


'''
Обучаем модель
'''


df = pd.read_csv('./train/train.csv',
                 sep='\t',
                 encoding='utf-8',
                 usecols=['A', 'B', 'C', 'Y'])

train_y = df['Y']
train_X = df.drop('Y', axis=1)

model = LinearRegression()
model.fit(train_X, train_y)

pkl_filename = 'pickle_model.pkl'
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)
