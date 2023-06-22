# Импорт необходимых библиотек
import numpy as np
import pandas as pd
import os

# Создание обучающей выборки
train_data = pd.DataFrame({
    'price': np.round(np.random.normal(650000, 100000, 1000)),
    'delivery_time': np.round(np.random.normal(25, 10, 1000)),
    'number_of_transit_nodes': np.round(np.random.normal(3, 2, 1000)),
})

# Добавление метки в train в зависимости от времени доставки
train_data['label'] = np.where(train_data['delivery_time'] > 25, 1, 0)

# Создание тестовой выборки
test_data = pd.DataFrame({
    'price': np.round(np.random.normal(650000, 100000, 500)),
    'delivery_time': np.round(np.random.normal(25, 10, 500)),
    'number_of_transit_nodes': np.round(np.random.normal(3, 2, 500)),
})

# Добавление метки в test в зависимости от времени доставки
test_data['label'] = np.where(test_data['delivery_time'] > 25, 1, 0)

# Создание папок train и test
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')

# Сохранение данных в файлы
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
