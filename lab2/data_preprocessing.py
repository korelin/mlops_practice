import pandas as pd
from sklearn.preprocessing import StandardScaler

# Загружаем тренировочную и тестовую выборки.
train_data = pd.read_csv('train/data.csv')
test_data = pd.read_csv('test/data.csv')

# Выполняем предобработку данных.
scaler = StandardScaler().fit(train_data[['x', 'y']])
train_data[['x', 'y']] = scaler.transform(train_data[['x', 'y']])
test_data[['x', 'y']] = scaler.transform(test_data[['x', 'y']])

# Записываем предобработанные данные в соответствующие файлы.
train_data.to_csv('train/preprocessed_data.csv', index=False)
test_data.to_csv('test/preprocessed_data.csv', index=False)
