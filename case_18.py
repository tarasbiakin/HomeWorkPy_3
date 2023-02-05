# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите число N ')) 
x = int(input('Введите число Х ')) 


def Result(n,x):
    list_1 = []
    k = -1

    for i in range(1,n+1):
        # list_1.append(i)
        list_1.append(random.randint(1, n+1))
    # print(list_1)

    for i in range (len(list_1)):
        if list_1[i] == x+1:
            k=list_1[i]
            if k == -1:
                return("Такого числа нет")
            else:
                return k
        
  
    
print(f'Самый близкий элемент списка к число {x} равен {Result(n,x)} ')   
           