import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Загрузка данных из файлов
train_data = pd.read_csv('train/train_data.csv')
test_data = pd.read_csv('test/test_data.csv')

# Масштабирование признаков
scaler = StandardScaler()
train_data[['temperature', 'humidity', 'pressure']] = scaler.fit_transform(train_data[['temperature', 'humidity', 'pressure']])
test_data[['temperature', 'humidity', 'pressure']] = scaler.transform(test_data[['temperature', 'humidity', 'pressure']])

# Сохранение масштабированных данных в файлы
if not os.path.exists('train_preprocessed'):
    os.makedirs('train_preprocessed')
if not os.path.exists('test_preprocessed'):
    os.makedirs('test_preprocessed')

train_data.to_csv('train_preprocessed/train_data_preprocessed.csv', index=False)
test_data.to_csv('test_preprocessed/test_data_preprocessed.csv', index=False)
