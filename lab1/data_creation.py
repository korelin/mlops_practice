import os
import tensorflow as tf


#print("data_creation.py dummy output")

SOURCE_URL = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
SOURCE_FOLDER = "PetImages"

folders = ("train","test")

source_file_name = os.path.basename(SOURCE_URL)

initial_path = os.getcwd()
working_path = os.path.dirname(os.path.abspath(__file__))


os.chdir(working_path) # set directory of the script as current

# Очищаем workspace от скачанного файла от предыдущих запусков.
os.system('rm -f {0}'.format(source_file_name))

# Очищаем workspace от распакованного датасета от предыдущих запусков.
os.system("rm -rf {0}".format(SOURCE_FOLDER))

# удаляем папки с train и test датасэтами
for folder in folders:
    os.system("rm -rf {0}".format(folder))

# Скачиваем датасет
os.system('curl -O {0}'.format(SOURCE_URL))

# Распаковываем датасет.
os.system("unzip -q {0} '{1}/**/*'".format(source_file_name, SOURCE_FOLDER))

# get list of source subfolders = list of categories
source_categories = os.listdir(SOURCE_FOLDER)
# make indexes the same as tf will generate besed on alphabetic order
source_categories.sort()
print("source categories=", source_categories)

# replicate SOURCE_FOLDER structure
for folder in folders:
    os.mkdir(folder)
    for category in source_categories:
        os.mkdir("{0}/{1}".format(folder, category))

# Отфильтруем изображения, у которых в заголовке нет JFIF.
# Нам нужна информация о разрешении и соотношении сторон.
for folder_name in source_categories:
    del_img_cnt = 0
    for file_name in os.listdir(f"{SOURCE_FOLDER}/{folder_name}"):
        file_path = f"{SOURCE_FOLDER}/{folder_name}/{file_name}"
        # Используем менеджер контекста (with) при чтении файла.
        # Файл будет закрыт автоматически при выходе из блока кода.
        with open(file_path, "rb") as file:
            # Ищем в первых 4 байтах файла байты "JFIF"
            has_jfif = tf.compat.as_bytes("JFIF") in file.peek(4)
            if not has_jfif:
                file.close()
                os.remove(file_path)
                del_img_cnt += 1
    print(f"Удалено {del_img_cnt} изображений из {folder_name}")

# Генерируем обучающую и валидационной выборки.
VALIDATION_SPLIT = 0.2
SEED = 1337
IMAGE_SIZE = (180, 180)
BATCH_SIZE = 64 # размер кэша при чтении с диска

# Keras понимает, что 2 класса, потому что 2 директории (Cats, Dogs).
# Автоматически будут созданы два лейбла (0 - Cat, 1 - Dog).

training_images = tf.keras.preprocessing.image_dataset_from_directory(
    SOURCE_FOLDER,
    validation_split = VALIDATION_SPLIT,
    subset = "training",
    seed = SEED,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
)

validation_images = tf.keras.preprocessing.image_dataset_from_directory(
    SOURCE_FOLDER,
    validation_split = VALIDATION_SPLIT,
    subset = "validation",
    seed = SEED,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
)
cnt = 0

# save train dataset
for images, labels in training_images.take(-1):
    for i in range(images.shape[0]):
        tf.keras.preprocessing.image.save_img(
            f'train/{source_categories[labels[i]]}/{cnt}.jpg', images[i])
        cnt += 1
# save test dataset
for images, labels in validation_images.take(-1):
    for i in range(images.shape[0]):
        tf.keras.preprocessing.image.save_img(
            f'test/{source_categories[labels[i]]}/{cnt}.jpg', images[i])
        cnt += 1

os.chdir(initial_path) # set initial directory as current