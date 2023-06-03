#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# %% Импорт
import argparse
import os
import sys

from data_methods import make_data, devide_save


# %% Задание пути для сохранения файлов
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
    file_path=f"{file_path}/"

#%% Если пути не существует, скрипт прерывает свою работу
if (not os.path.isdir(file_path)) or \
        (not os.path.isdir(file_path + 'train/')) or \
        (not os.path.isdir(file_path + 'test/')):
    print("There is no such path")
    sys.exit(1)

# %% Генерация данных

# Количество данных
count = 15000

# Зерно генератора случайных чисел
seed = 38

dataset_data = devide_save(*make_data(count, method='moons',
                                    noises=0.15, random_state=seed), file_path, dataset_name)

if dataset_data is None:
    sys.exit(2)
