import pandas as pd
import pickle

# Загрузка обработанных данных из файлов
test_data = pd.read_csv('test_preprocessed/test_data_preprocessed.csv')

# Загрузка модели из файла
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Тестирование модели
X_test = test_data[['temperature', 'humidity', 'pressure']]
y_test = test_data['label']
accuracy = model.score(X_test, y_test)

# Вывод результатов тестирования
print("Model test accuracy is:", accuracy)
