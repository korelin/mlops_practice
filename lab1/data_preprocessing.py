import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Загрузка данных обучающего и тестового
# наборов из файлов CSV для анализа и обработки.
train_data = pd.read_csv('train/train_data.csv')
test_data = pd.read_csv('test/test_data.csv')

# Выполнение стандартизации признаков
# "price" (стоимость доставки), "delivery_time" (длительность доставки) и "number_of_transit_nodes" (количество транзитных узлов)
# в обучающем и тестовом наборах данных.
scaler = StandardScaler()
train_data[['price', 'delivery_time', 'number_of_transit_nodes']] = scaler.fit_transform(train_data[['price', 'delivery_time', 'number_of_transit_nodes']])
test_data[['price', 'delivery_time', 'number_of_transit_nodes']] = scaler.transform(test_data[['price', 'delivery_time', 'number_of_transit_nodes']])

# Проверка наличия двух директорий:
# 'train_preprocessed' и 'test_preprocessed',
# для целей сохранения предобработанных данных обучающего и тестового наборов.
if not os.path.exists('train_preprocessed'):
    os.makedirs('train_preprocessed')
if not os.path.exists('test_preprocessed'):
    os.makedirs('test_preprocessed')

# Сохраненение предобработанных данные обучающего
# и тестового наборов в формате CSV
train_data.to_csv(
    'train_preprocessed/train_data_preprocessed.csv', index=False
    )
test_data.to_csv(
    'test_preprocessed/test_data_preprocessed.csv', index=False
    )
