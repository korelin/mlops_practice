import numpy as np
import pandas as pd
import os

# Создание обучающей выборки
train_data = pd.DataFrame({
    'temperature': np.random.normal(loc=25, scale=5, size=1000),
    'humidity': np.random.normal(loc=50, scale=10, size=1000),
    'pressure': np.random.normal(loc=1000, scale=50, size=1000)
})
train_data['label'] = np.where(train_data['temperature'] > 30, 1, 0) # Добавляем метку в зависимости от температуры

# Создание тестовой выборки
test_data = pd.DataFrame({
    'temperature': np.random.normal(loc=25, scale=5, size=500),
    'humidity': np.random.normal(loc=50, scale=10, size=500),
    'pressure': np.random.normal(loc=1000, scale=50, size=500)
})
test_data['label'] = np.where(test_data['temperature'] > 30, 1, 0)

# Создание папок train и test
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')

# Сохранение данных в файлы
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
