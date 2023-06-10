import pandas as pd

# Загружаем датасет из файла.
titanic_df = pd.read_csv('datasets/data.csv')

# Заполняем пропущенные значения возраста средним значением.
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)

# Записываем измененный датасет в файл.
titanic_df.to_csv('datasets/data.csv', index=False)
