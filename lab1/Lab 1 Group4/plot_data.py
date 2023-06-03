import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_data(dataset, dataset_name, i=0):
    """
    Вывод графиков для 3-х наборов данных
    :param dataset: Дата-фрейм набора данных
    :param dataset_name: Название дата-фрейма набора данных
    :param i: Номер набора: 0 - обучающий, 1- тестовый
    :return: Выводит 3 графика
    """
    colors = ("#FF0000", '#0000FF')
    alpha = 0.7
    s = 5
    cm_bright = ListedColormap(colors)

    plt.figure(figsize=(30, 8))

    plt.scatter(dataset[i]['x'].values, dataset[i]['y'].values, marker='o', c=dataset[i]['z'].values,
                cmap=cm_bright, s=s, alpha=alpha)
    plt.title(dataset_name)

    plt.show()
