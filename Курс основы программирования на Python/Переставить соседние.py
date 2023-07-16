# Курс основы программирования на Python
# Задание по программированию: Переставить соседние
# 09.05.2019
#
# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
#
# Формат ввода
#
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Формат вывода
#
# Выведите ответ на задачу.

numList = list(map(int, input().split()))
numList.reverse()
complList = []
if len(numList) % 2 == 0:
    while len(numList) != 0:
        a = numList.pop()
        b = numList.pop()
        complList.append(b)
        complList.append(a)
else:
    while len(numList) != 1:
        a = numList.pop()
        b = numList.pop()
        complList.append(b)
        complList.append(a)
    complList.append(numList.pop())
print(*complList)
