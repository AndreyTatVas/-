# Курс основы программирования на Python
# Задание по программированию: Сортировка подсчетом
# 15.05.2019
#
# Дан список из N (N≤2*10⁵) элементов, которые
# принимают целые значения от 0 до 100.
#
# Отсортируйте этот список в порядке неубывания
# элементов. Выведите полученный список.
#
# Решение оформите в виде функции CountSort(A),
# которая модифицирует передаваемый ей список.
# Использовать встроенные функции сортировки нельзя.


def countSort(a):
    """Функция для сортировки подсчетом"""
    cntMarks = [0] * 101
    for i in a:
        cntMarks[i] += 1
    for nowMark in range(101):
        print((str(nowMark) + ' ') * cntMarks[nowMark], end='', file=onFile)


# inFile - Файл с исходными данными
# onFile - Файл с конечнымии данными
# numInput - список чисел полученых из файла inFile

inFile = open('input.txt', 'r', encoding='utf8')
onFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readline()
numInput = map(int, lines.split())

countSort(numInput)
inFile.close()
onFile.close()
