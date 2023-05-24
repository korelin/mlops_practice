import os
import pickle
import pandas as pd

# Загружаем предобработанные данные тестовой выборки.
test_data = pd.read_csv('test/preprocessed_data.csv')

# Загружаем модель и оцениваем ее результативность на тестовой выборке.
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
metric_value = model.score(test_data[['x']], test_data['y'])
print(f"Model test accuracy is: {metric_value:.3f}")
