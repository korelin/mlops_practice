import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# Загружаем предобработанные данные.
train_data = pd.read_csv('train/preprocessed_data.csv')

# Обучаем модель и сохраняем результаты с помощью модуля pickle.
model = LinearRegression().fit(train_data[['x']], train_data['y'])
pickle.dump(model, open('model.pkl', 'wb'))
