# Курс основы программирования на Python
# Задание по программированию: Встречалось ли число раньше
# 17.05.2019
#
# Во входной строке записана последовательность чисел
# через пробел. Для каждого числа выведите слово
# YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если
# не встречалось.
#
# Формат ввода
#
# Вводится список чисел. Все числа списка находятся
# на одной строке.
#
# Формат вывода
#
# Выведите ответ на задачу.
#
# inFile - Файл с исходными данными
# onFile - Файл с конечнымии данными
# numInput - список чисел из файла input.txt
# resSet - множество списка numInput
#
inFile = open('input.txt', 'r', encoding='utf8')
onFile = open('output.txt', 'w', encoding='utf8')
numInput = list(map(int, inFile.readline().split()))
resSet = set()
for num in numInput:
    if num in resSet:
        print('YES', file=onFile)
    else:
        print('NO', file=onFile)
    resSet.add(num)

onFile.close()
inFile.close()