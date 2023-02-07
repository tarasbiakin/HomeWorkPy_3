# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input('Введите размер списка '))
min = float (input('Введите нижнюю границу '))
max = float (input('Введите верхнюю границу '))

def Сomposition(n,min,max):
    list_1 = []
    
    
    for i in range(n):
        list_1.append(random.uniform(min, max))
    print(list_1)
    for i in range(len(list_1)):
        if list_1[i]>max:
            max = list_1[i]
            
    for i in range(len(list_1)):
        if list_1[i]<min:
            min = list_1[i]
            
    a = max*min
    return a

print(f'Произведение максимума и минимума {Сomposition(n,min,max)}')   
