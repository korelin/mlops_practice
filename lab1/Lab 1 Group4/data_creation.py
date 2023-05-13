#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import argparse
import os
# %% Импорт
import sys

from generate_data import make_data, devide_save
from plot_data import plot_data


# %% Задание пути для сохранения файлов
file_path = os.getcwd()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    namespace = parser.parse_args()

    if namespace.dir:
        file_path = namespace.dir

# Если пути не существует, скрипт прерывает свою работу
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

moons_data = devide_save(*make_data(count, method='moons',
                                    noises=0.15, random_state=seed), file_path, 'moons')
if moons_data is None:
    sys.exit(2)

circles_data = devide_save(*make_data(count, method='circles',
                                      noises=0.15, random_state=seed), file_path, 'circles')
if circles_data is None:
    sys.exit(2)

line_data = devide_save(*make_data(count, method='line',
                                   noises=0.15, random_state=seed), file_path, 'line')
if line_data is None:
    sys.exit(2)

# %% Вывод графиков
show_plots = False
if show_plots:
    plot_data(moons_data, circles_data, line_data, 0)
    plot_data(moons_data, circles_data, line_data, 1)
