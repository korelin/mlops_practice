import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Загрузка обработанных данных из файлов
train_data = pd.read_csv('train_preprocessed/train_data_preprocessed.csv')

# Обучение модели
X_train = train_data[['temperature', 'humidity', 'pressure']]
y_train = train_data['label']
model = LogisticRegression()
model.fit(X_train, y_train)

# Сохранение модели в файл
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
