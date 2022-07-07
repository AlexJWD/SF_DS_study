"""Игра угадай число
Компьютер сам загадывает и сам угадывает число от 1 до 100
"""

import numpy as np


def higher_lower_predict(number: int = 1) -> int:
    """Угадываем число, используя проверку "больше-меньше" и сужая интервал поиска пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_level , max_level = 1 , 100 # границы коридора возможных значений
    predict_number = (max_level + min_level)//2
    
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min_level = predict_number
            predict_number = (max_level + min_level)//2 + (max_level + min_level)%2 # округляем в большую сторону
        else:
            max_level = predict_number
            predict_number = (max_level + min_level)//2 # округляем в меньшую сторону
             
    return count


def score_game(higher_lower_predict) -> int:
    """За какое среднее количество попыток алгоритм угадывает 1000 случайных чисел от 1 до 100

    Args:
        higher_lower_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(higher_lower_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(higher_lower_predict)
