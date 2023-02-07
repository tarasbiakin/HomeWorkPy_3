# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input('Введите размер списка '))

def SuM(n):
    list_1 = []
    sum = 0
    for i in range(n):
        list_1.append(random.randint(-10, 10))
    print(list_1)
    for i in range(len(list_1)):
        if i%2!=0:
            sum= sum+list_1[i]
    return sum

print(f'Сумма элементов стоящих на нечетных позициях равна {SuM(n)}')   

