import pandas as pd

# Загружаем датасет из файла.
titanic_df = pd.read_csv('datasets/data.csv')

# Оставляем только нужные столбцы.
titanic_df = titanic_df[['Pclass', 'Sex', 'Age']]

# Записываем измененный датасет в файл.
titanic_df.to_csv('datasets/data.csv', index=False)
