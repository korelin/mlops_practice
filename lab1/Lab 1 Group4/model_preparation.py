#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Импортируем нужные библиотеки"""
import argparse
import os
import sys
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression

#Задаем путь для сохранения модели, а так же пути для чтения датасета
file_path = os.getcwd()
dataset_name = 'moons'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    parser.add_argument('-t', '--type')
    namespace = parser.parse_args()

    if namespace.dir:
        file_path = namespace.dir

    if namespace.type:
        dataset_name = namespace.type

if not file_path.endswith("/"):
    file_path = f"{file_path}/"

#%% Если пути не существует, скрипт прерывает свою работу
if (not os.path.isdir(file_path)) or \
        (not os.path.isdir(file_path + 'train/')) or \
        (not os.path.isdir(file_path + 'test/')):
    print("There is no such file")
    sys.exit(1)

#%% Загрузим, обучим и сохраним модель
def train_and_save_model(X_train, y_train, file_path, file_name):
    """
    :param X_train: x, y params of dataset
    :param y_train: target
    :param file_path: path to content folder
    :param file_name: name of opened file
    """
    model = LogisticRegression(max_iter=100_000).fit(X_train, y_train)
    file_name = file_name.replace("_stand.csv", "_model.pkl")
    file_path = file_path + file_name
    try:
        pickle.dump(model, open(file_path, 'wb'))
        print(f"Model succesfully generated {file_path}")
        return  model
    except:
        print(f"Ошибка сохранения файла {file_name}")
        return None

for filename in os.listdir(file_path + "train/"):
    if filename.endswith("_stand.csv"):
        full_filename = f"{file_path}train/{filename}"
        data_train = pd.read_csv(full_filename)

        X_train = data_train[['x', 'y']].values
        y_train = data_train['z'].values
        model = train_and_save_model(X_train, y_train, file_path, filename)

        if model is None:
            sys.exit(3)
