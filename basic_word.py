# basic_word.py
#Класс_BasicWord
class BasicWord:
    """Класс для хранения исходного слова и его допустимых подслов типа запчастей или деталей"""
    
    def __init__(self, word, subwords):
        """
        Инициализация экземпляра BasicWord
        
        Args:
            word (str): исходное слово
            subwords (list): список допустимых подслов типа пазлы для картины - главного слова
        """
        self.word = word
        self.subwords = subwords
    
    def check_word(self, user_word):
        """
        Проверим, есть ли тут введенное слово в списке допустимых подслов - т.е.отсюда subwords (list)
        
        Args:
            user_word (str): слово для проверки
            
        Returns:
            bool: True если слово есть в списке, тогда - неправильно т.е. фальшиво False
        """
        return user_word in self.subwords
    
    def count_subwords(self):
        """
        Это строка вернёт количество допустимых подслов
        
        Returns:
            int: количество подслов
        """
        return len(self.subwords)
    
    def __repr__(self):
        return f"BasicWord(word='{self.word}', subwords_count={self.count_subwords()})"