"""
Методы генерации данных
"""
import numpy as np
import pandas as pd
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.model_selection import train_test_split


def make_data(count, method='line', noises=0.15, random_state=42):
    """
    Создание набора данных для бинарной классификации
    :param count: количество точек
    :param method: тип набора данных
    :param noises: коэффициент ~ сила шума
    :param random_state: фиксированный сид случайных чисел (для повторяемости)
    :return: три numpy массива значений x, y и класса
    """
    if random_state:
        np.random.RandomState(seed=random_state)

    data_cls = np.array([])
    xy = np.array([])

    if method == 'line' or method is None:
        # если выбран метод line (или никакой не задан),
        # то мы создаем набор данных с использованием функции make_classification
        # это будут линейно-разделимые данные
        xy, data_cls = make_classification(n_samples=count,  # количество точек
                                           n_features=2,  # количество признаков
                                           n_redundant=0,  # количество бесполезных признаков
                                           n_informative=2,  # количество информативных признаков
                                           n_clusters_per_class=1,  # количество групп точек на класс
                                           class_sep=2,  # количество классов
                                           random_state=random_state  # фиксированный сид случайных чисел
                                           )

    elif method == 'moons':
        # если выбран метод moons,
        # то мы создаем набор данных с использованием функции make_moons
        # это будут данные похожие на Инь-Ян
        xy, data_cls = make_moons(n_samples=count,  # количество точек
                                  noise=noises,  # уровень шума
                                  random_state=random_state  # фиксированный сид случайных чисел
                                  )

    elif method == 'circles':
        # если выбран метод circles,
        # то мы создаем набор данных с использованием функции make_circles
        # это будут данные в виде концентрических окружностей
        xy, data_cls = make_circles(n_samples=count,  # количество точек
                                    noise=noises,  # уровень шума
                                    factor=0.5,  # соотношение радиусов внутренней и внешней окружности
                                    random_state=random_state  # фиксированный сид случайных чисел
                                    )

    if np.size(xy) > 2 and xy.shape[1] > 1 and np.size(data_cls) > 2:
        return xy[:, 0], xy[:, 1], data_cls

    return None


def devide_save(x, y, data_cls, data_path, name, random_state=42):
    """
     Разделение на обучающую и тестовую выборки и
     сохранение данных в файлы
    :param x: numpy массив значений x
    :param y: numpy массив значений y
    :param data_cls:  numpy массив значений класса
    :param data_path:  адрес директории для сохранений файлов
    :param name: название файла для сохранения
    :param random_state: фиксированный сид случайных чисел (для повторяемости)
    :return: Два дата-фрейма с обучающими и тесовыми данными
    """

    x_train, x_test, y_train, y_test, z_train, z_test = train_test_split(x, y, data_cls, test_size=0.3,
                                                                         random_state=random_state)
    file_path = ""
    try:
        df_train = pd.DataFrame({'x': x_train, 'y': y_train, 'z': z_train})
        file_path = data_path + 'train/' + name + '.csv'
        df_train.to_csv(file_path, index=False)

        df_test = pd.DataFrame({'x': x_test, 'y': y_test, 'z': z_test})
        file_path = data_path + 'test/' + name + '.csv'
        df_train.to_csv(file_path, index=False)

        return df_train, df_test

    except:
        print(f"Ошибка сохранения файла {file_path}")
        return None
