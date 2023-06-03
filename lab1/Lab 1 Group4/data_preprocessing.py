#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# %% Импорт
import sys
import argparse
import os
from sklearn.preprocessing import StandardScaler

from data_methods import transforms
from plot_data import plot_data

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
    file_path = f"{file_path}/"

# %% Если пути не существует, скрипт прерывает свою работу
if (not os.path.isdir(file_path)) or \
        (not os.path.isdir(file_path + 'train/')) or \
        (not os.path.isdir(file_path + 'test/')):
    print("There is no such path")
    sys.exit(1)

show_plots = False

scaler = StandardScaler(copy=True, with_mean=True, with_std=True)

for filename in os.listdir(file_path + "test/"):
    if filename.endswith("_source.csv"):
        full_filename = f"{file_path}test/{filename}"
        dataset_data = transforms(full_filename, scaler)
        if dataset_data is None:
            sys.exit(2)

        # %% Вывод графиков
        if show_plots:
            plot_data(dataset_data, dataset_name + "_test")

for filename in os.listdir(file_path + "train/"):
    if filename.endswith("_source.csv"):
        full_filename = f"{file_path}train/{filename}"
        dataset_data = transforms(full_filename, scaler)
        if dataset_data is None:
            sys.exit(2)

        # %% Вывод графиков
        if show_plots:
            plot_data(dataset_data, dataset_name + "_train")