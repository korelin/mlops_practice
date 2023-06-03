"""Импортируем нужные библиотеки"""
import os

import pandas as pd
import pickle
import data_creation as dc
from sklearn.linear_model import LogisticRegression

#Задаем путь для сохранения модели, а так же пути для чтения датасета, пока что хардкод, 04.06 я бы задал пару вопросов
file_path = f'{os.getcwd()}\\train\\moons.csv'
dataset_name = dc.dataset_name

model_path = os.getcwd()

# прочитаем из csv файла подготовленный датасет для обучения
data_train = pd.read_csv(file_path)
X_train = data_train[['x', 'y']].values
y_train = data_train['z'].values

# загрузим, обучим и сохраним модель
def train_and_save_model():
    """"Загрузка, обучение и сохранение модели"""
    model = LogisticRegression(max_iter=100_000).fit(X_train, y_train)
    pickle.dump(model, open('model.pkl', 'wb'))

train_and_save_model()