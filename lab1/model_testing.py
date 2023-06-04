import os
import tensorflow as tf


#print("model_testing.py dummy output")


initial_path = os.getcwd()
working_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(working_path)

TRAIN_FOLDER = "train"
MODEL_FOLDER = "xception_network_cats_and_dogs"
CHECKPOINTS_FOLDER = "xception_network_cats_and_dogs_checkpoints"

IMAGE_SIZE = (180, 180)
BATCH_SIZE = 64

validation_images = tf.keras.utils.image_dataset_from_directory(
    TRAIN_FOLDER,
    labels='inferred',
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
)

# Буферизируем ввод.
validation_images = validation_images.prefetch(buffer_size=BATCH_SIZE)


# загружаем заранее обученную модель целиком из формата TensorFlow (saved_model.pb + variables/).
# в тензорфлоу выгружается и структура нейросети и коэффициенты
xception_network_cats_and_dogs = tf.keras.models.load_model(MODEL_FOLDER)

xception_network_cats_and_dogs.evaluate(validation_images)


os.chdir(initial_path)