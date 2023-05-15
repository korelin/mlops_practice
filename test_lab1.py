import os


# Функция проверки существования файла lab1/train/train_data.csv
def test_train_data_file_exists():
    assert os.path.exists('lab1/train/train_data.csv'),
    "File train/train_data.csv does not exist."

# Функция проверки существования файла lab1/test/test_data.csv
def test_test_data_file_exists():
    assert os.path.exists('lab1/test/test_data.csv'),
    "File test/test_data.csv does not exist."

# Запуск функций проверки
if __name__ == '__main__':
    test_train_data_file_exists()
    test_test_data_file_exists()
    print("All tests passed successfully.")
