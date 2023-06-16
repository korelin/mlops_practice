
# Загружаем тренировочный и тестовый датасеты и объединяем их в один.
titanic_train, titanic_test = titanic()
titanic_df = pd.concat([titanic_train, titanic_test], ignore_index=True)

# Записываем полученный датасет в файл.
titanic_df.to_csv('datasets/data.csv', index=False)
