
'''
в data_creation.py производит только загрузку исходны данных
и распаковку

Разделение дынных на train и test вынесено в data_preprocessing.py
согласно формулировке задания в Модуле 2 т.к. это более оптимальное
разделение с точки зрения выполняемых действий и потребляемых ресурсов
'''

import os


#print("data_creation.py dummy output")

SOURCE_URL = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
SOURCE_FOLDER = "PetImages"

source_file_name = os.path.basename(SOURCE_URL)

initial_path = os.getcwd()
working_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(working_path) # set directory of the script as current


# Очищаем workspace от скачанного файла от предыдущих запусков.
os.system('rm -f {0}'.format(source_file_name))

# Очищаем workspace от распакованного датасета от предыдущих запусков.
os.system("rm -rf {0}".format(SOURCE_FOLDER))

# Скачиваем датасет
os.system('curl -O {0}'.format(SOURCE_URL))

# Распаковываем датасет.
os.system("unzip -q {0} '{1}/**/*'".format(source_file_name, SOURCE_FOLDER))


os.chdir(initial_path) # set initial directory as current