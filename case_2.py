# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите размер списка '))

def Сomposition(n):
    list_1 = []
    сomposition = 0
    for i in range(n):
        list_1.append(random.randint(-10, 10))
    print(list_1)
    сomposition = list_1[0]*list_1[n-1]
    return сomposition

print(f'Произведение первого и последнего элемента равно {Сomposition(n)}')   

