#СкайПро_Курс_2_Курсовая_работа_Олег_Васильеич_С
#файл_самой_игрушки

# main.py
from player import Player
from utils import load_random_word

def main():
    """Основная функция игры"""
    
    # Шаг 4: Стартовая логика
    print("Программа: Прошу Введите имя")
    #удалить символы только в конце строки - это будет делать .strip(), вдруг будет введён пробел
    player_name = input("Пользователь: ").strip()
    
    # Создаем экземпляр Player
    player = Player(player_name)
    
    # Загружаем случайное слово
    current_word = load_random_word()
    
    # Приветствие
    print(f"Программа: Привет, {player_name}!")
    print(f"Программа: Составьте {current_word.count_subwords()} слов из слова {current_word.word.upper()}")
    print("Программа: Слова должны быть не короче 3 букв")
    print("Программа: Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Программа: Теперь, ваше первое слово? набирайте")
    
    # Шаг 5: Основной игровой цикл
    while player.get_used_words_count() < current_word.count_subwords():
        user_input = input("Пользователь: ").strip().lower()
        
        # Проверим на остановку игры если набрано слово Стоп или Stop
        if user_input in ["stop", "стоп"]:
            print(f"\nПрограмма: Игра прервана. Вы угадали {player.get_used_words_count()} слов из {current_word.count_subwords()}")
            break
        
        # Проверка длины слова , если слово меньше , чем из трёх буковок
        if len(user_input) < 3:
            print("Программа: очень короткое слово")
            continue
        
        # Проверяю, есть ли слово в допустимых подсловах , которые уже есть в списке
        if not current_word.check_word(user_input):
            print("Программа: неверно")
            continue
        
        # Проверяю не использовалось ли слово раньше или нет ещё
        if player.is_word_used(user_input):
            print("Программа: это слово уже использовалось")
            continue
        
        # Если все проверки пройдены - слово угадано верно
        player.add_word(user_input)
        print("Программа: верно")
    
    # Шаг 6: Вывод статистики (если игра завершилась не досрочно)
    if player.get_used_words_count() == current_word.count_subwords():
        print(f"\nПрограмма: Игра завершена, вы угадали {player.get_used_words_count()} слов!")

if __name__ == "__main__":
    main()