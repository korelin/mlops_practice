import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_data(moons_data, circles_data, line_data, i=0):
    """
    Вывод графиков для 3-х наборов данных
    :param moons_data: Дата-фрейм набора данных 'Инь-Ян (Moons)'
    :param circles_data:  Дата-фрейм второго набора данных 'Круги'
    :param line_data:  Дата-фрейм третьего набора данных 'Линейно разделимые'
    :param i: номер набора: 0 - обучающий, 1- тестовый
    :return: Выводит 3 графика
    """
    colors = ("#FF0000", '#0000FF')
    alpha = 0.7
    s = 5
    cm_bright = ListedColormap(colors)

    plt.figure(figsize=(30, 8))

    plt.subplot(1, 3, 1)
    plt.scatter(moons_data[i]['x'].values, moons_data[i]['y'].values, marker='o', c=moons_data[i]['z'].values,
                cmap=cm_bright, s=s, alpha=alpha)
    plt.title('Инь-Ян (Moons)')

    plt.subplot(1, 3, 2)
    plt.scatter(circles_data[i]['x'].values, circles_data[i]['y'].values, marker='o', c=circles_data[i]['z'].values,
                cmap=cm_bright, s=s, alpha=alpha)
    plt.title('Круги')

    plt.subplot(1, 3, 3)
    plt.scatter(line_data[i]['x'].values, line_data[i]['y'].values, marker='o', c=line_data[i]['z'].values,
                cmap=cm_bright, s=s, alpha=alpha)
    plt.title('Линейно разделимые')

    plt.show()
