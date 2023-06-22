import os
import random
import numpy as np
import pandas as pd

data_file = 'data.csv'
train_data_folder = 'train'
test_data_folder = 'test'

# Проверим, существуют ли папки для тернировочных и тестовых выборок.
# Если нет, создадим их. 
if not os.path.exists('train'):
    os.mkdir('train')
if not os.path.exists('test'):
    os.mkdir('test')

# Генерируем значения предиктора x.
x_min = 0
x_max = 20
x = np.array([random.randint(x_min, x_max) for i in range(50)])

# Генерируем шум. 
noise = 200
e = np.array([random.randint(-noise, noise) for i in range(50)])

# Генерируем значения целевой переменной y.
b_0 = 10
b_1 = 15
y = b_0 * x + b_1 + e / 10

# Объединяем x и y в датафрейм.
data = pd.DataFrame({'x': x, 'y': y})

# Разбиваем данные на тренировочную и тестовую выборки.
train_size = int(0.8 * len(data))
train_data = data.iloc[:train_size]
test_data = data.iloc[train_size:]

# Записываем выборки в соответствующие файлы.
train_data.to_csv('train/data.csv', index=False)
test_data.to_csv('test/data.csv', index=False)
