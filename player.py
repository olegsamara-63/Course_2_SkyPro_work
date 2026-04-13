

# player.py
class Player:
    """Класс для хранения информации об игроке  - типа Плеер и его угаданных словах"""
    
    def __init__(self, name):
        """
        Инициализация экземпляра Player - не уверен , в слове Player - 
        вдруг оно зарезервированное, чёрт его знает
        
        Args:
            name (str): имя пользователя, точнее игрока 
        """
        self.name = name
        self.used_words = []
    
    def get_used_words_count(self):
        """
        Должно вернуть то количество использованных 
        (угаданных , если уже воодил пользователь) слов
        
        Returns:
            int: количество использованных слов
        """
        return len(self.used_words)
    
    def add_word(self, word):
        """
        Добавляет слово в список использованных слов
        
        Args:
            word (str): слово для добавления того бреда , что Плеер уже вводил 
        """
        if word not in self.used_words:
            self.used_words.append(word)
    
    def is_word_used(self, word):
        """
        Проверим, было ли уже  это слово раньше, ввоодилось или нет уже
        
        Args:
            word (str): слово для проверки
            
        Returns:
            bool: True если слово уже использовано, ну тогда всё - фальшивка False
        """
        return word in self.used_words
    
    def __repr__(self):
        return f"Player(name='{self.name}', used_words_count={self.get_used_words_count()})"