import pandas as pd  # для работы с табличными данными
# Классификатор логистической регрессии
from sklearn.linear_model import LogisticRegression
import pickle  # для (де)сериализации объектов


# Загрузка обработанных трен-х данных из файла train_data_preprocessed.csv
train_data = pd.read_csv('train_preprocessed/train_data_preprocessed.csv')

# Сохранение признаков стоимость доставки, длительность доставки, количество транзитных узлов
X_train = train_data[['price', 'delivery_time', 'number_of_transit_nodes']]

# Сохранение целевой метки
y_train = train_data['label']

# Создание модели логистической регрессии
model = LogisticRegression()

# Обучение модели на тренировочных данных
model.fit(X_train, y_train)

# Сохранение модели в файл model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
