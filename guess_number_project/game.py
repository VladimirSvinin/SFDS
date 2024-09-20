"""Игра угадай число"""

import numpy as np # Импорт необходимой библиотеки
import math #загружаем библиотеку для округления вверх с помощтю функции .ceil()


def random_predict(number: int = 1) -> int:
    """загадываем число, которое нужно будет угадать
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток (count)
    """

    # количество попыток
    count = 0

    predict = np.random.randint(1, 101)  # создаём случайное число, которое мы будем сравнивать  с number
    print(f'number = {number}')
    print(f'predict = {predict}')

    while number != predict: 

        count +=1 # Запускам цикл, который повторяется до тех пор, пока условие верно
        if number > predict: predict = math.ceil((number + predict) / 2)
    # Если number > predict, то находим среднее арифметическое между ними и округляем вверх
    # Через несколько попыток predict = number
        else: predict = round((predict + number) / 2) # в случае, если number < predict - ситуация обратная
    # находим среднее арифметическое между 2 числами, округляя вниз и рано или поздно получим нужный результат
    return count
