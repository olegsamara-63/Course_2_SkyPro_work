#СкайПро_Курс_2_Курсовая_работа_Олег_Васильеич_С
#Функция load_random_word - выбор случаен типа того. Рандомный как то так
# utils.py
import random
from basic_word import BasicWord
from data import WORDS_DATA

def load_random_word():
    """
    Берём список слов  из data.py,
    случайное слово и надо создать экземпляр класса BasicWord
    
    Returns:
        BasicWord: экземпляр класса BasicWord со случайным словом 
        случайно выбранным так наверное правильно назвать
    """
    # Вместо внешнего ресурса использую свои придуманные  данные
    
    
    # Выбираю случайное слово из списка ВОРД ДАТЫ
    random_word_data = random.choice(WORDS_DATA)
    
    # Создаем экземпляр BasicWord
    basic_word = BasicWord(
        word=random_word_data["word"],
        subwords=random_word_data["subwords"]
    )
    
    return basic_word