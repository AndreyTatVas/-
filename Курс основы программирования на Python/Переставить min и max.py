# Курс основы программирования на Python
# Задание по программированию: Переставить min и max
# 09.05.2019
#
# В списке все элементы попарно различны. Поменяйте местами
# минимальный и максимальный элемент этого списка.
#
# Формат ввода
#
# Вводится список целых чисел. Все числа списка находятся на одной строке.
#
# Формат вывода
#
# Выведите ответ на задачу.

numList = list(map(int, input().split()))
minimum = min(numList)
maximum = max(numList)
for i in range(len(numList)):
    if numList[i] == minimum:
        minInd = i
    if numList[i] == maximum:
        maxInd = i
numList[minInd], numList[maxInd] = maximum, minimum
print(*numList)
