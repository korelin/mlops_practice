import pandas as pd

# Загружаем датасет из файла.
titanic_df = pd.read_csv('datasets/data.csv')

# Создаем новый признак с использованием one-hot-encoding для
# строкового признака “Пол”.
sex_dummies = pd.get_dummies(titanic_df.Sex)
titanic_df = pd.concat([titanic_df, sex_dummies], axis=1)

# Записываем измененный датасет в файл.
titanic_df.to_csv('datasets/data.csv', index=False)
