import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_data(dataset, dataset_name):
    """
    Вывод графиков для 3-х наборов данных
    :param dataset: Дата-фрейм набора данных
    :param dataset_name: Название дата-фрейма набора данных
    :return: Выводит 3 графика
    """
    colors = ("#FF0000", '#0000FF')
    alpha = 0.7
    s = 5
    cm_bright = ListedColormap(colors)

    plt.figure(figsize=(30, 8))

    plt.scatter(dataset.iloc[:,0].values, dataset.iloc[:,1].values, marker='o', c=dataset.iloc[:,2].values,
                cmap=cm_bright, s=s, alpha=alpha)
    plt.title(dataset_name)

    plt.show()
