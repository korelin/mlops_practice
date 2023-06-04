import streamlit as st
from sbert_punc_case_ru import SbertPuncCase
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import string


def check_input(input_text):
    """Пытаемся определить, на русском языке написан введенный текст,
    или нет.
    """
    return detect(input_text)


def text_punctuated(text_to_punctuate):
    """Преобразуем текст, проводя его через модель"""
    return model.punctuate(text_to_punctuate)


# Создаём объект - модель для преобразования текста
model = SbertPuncCase()

# Формируем заголовок для браузера
st.title("Восстанавление пунктуации текста")
st.subheader("Применяется после аудиораспознавания, а также при сомнениях \
    после перевода текста.")

# Забираем текст, введённый пользователем в браузере
input_text = st.text_area("Вставьте сюда текст на русском языке, например - \
    однако на улице прекрасная погода", value="")

# Проверяем, введен ли какой-нибудь текст.
# Если текст введен, то пробуем определить, на каком языке написан
# введенный текст.
# Если удалось определить, что текст не русский, выдаем сообщение
# об ошибке.
# Если удалось определить, что текст русский:
# обработаем текст, на случай, если пользователь ввёл не по правилам -
# преобразуем в нижний регистр и уберём знаки препинания.
# Пишем в браузере преобразованный текст.
# Если не удалось определить, на каком языке написан текст, выдаем
# сообщение об ошибке.
if len(input_text) > 0:
    try:
        detected_text = check_input(input_text)
        if detected_text != 'ru':
            st.error("Язык введенного текста не русский! Попробуйте ввести \
                текст еще раз.")
        else:
            lowercase_text = input_text.lower()
            text_to_punctuate = lowercase_text.translate(str.maketrans('', '',
                                                         string.punctuation))
            st.text_area("Преобразованный текст. Его можно выделить и \
                скопировать.",
                         value=text_punctuated(text_to_punctuate),
                         disabled=False)
    except LangDetectException:
        st.error("Невозможно определить язык! Попробуйте ввести текст еще \
            раз.")
