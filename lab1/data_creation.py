import pandas as pd
import numpy as np
import os

# Функция для создания набора данных
def create_temperature_dataset(start_date, end_date, anomaly=False, noise_level=0.0, freq='D'):
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    temperatures = np.sin(np.linspace(0, 3 * np.pi, len(dates))) * 10 + 20  # Пример изменения температуры

    if anomaly:
        # Вставка аномалии: случайный скачок температуры
        anomaly_days = np.random.choice(dates, size=5, replace=False)
        for day in anomaly_days:
            temperatures[dates == day] += np.random.randint(-5, 15)

    if noise_level > 0.0:
        noise = np.random.normal(0, noise_level, temperatures.shape)
        temperatures += noise

    return pd.DataFrame({'Date': dates, 'Temperature': temperatures})

# Создание обучающего и тестового наборов
train_data = create_temperature_dataset('2020-01-01', '2020-12-31', noise_level=2.5)
test_data = create_temperature_dataset('2021-01-01', '2021-12-31', anomaly=True, noise_level=2.5)

# Создание директорий для сохранения
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')

# Сохранение наборов данных
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)

print("Данные успешно созданы и сохранены.")
