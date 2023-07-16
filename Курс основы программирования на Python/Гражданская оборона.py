# Курс основы программирования на Python
# Задание по программированию: Гражданская оборона
# 14.05.2019
#
# Штаб гражданской обороны Тридесятой области решил
# обновить план спасения на случай ядерной атаки.
# Известно, что все n селений Тридесятой области
# находятся вдоль одной прямой дороги. Вдоль дороги
# также расположены m бомбоубежищ, в которых жители
# селений могут укрыться на случай ядерной атаки.
#
# Чтобы спасение в случае ядерной тревоги проходило
# как можно эффективнее, необходимо для каждого
# селения определить ближайшее к нему бомбоубежище.
#
# Формат ввода
#
# В первой строке вводится число n - количество селений
# (1 <= n <= 100000). Вторая строка содержит n различных
# целых чисел, i-е из этих чисел задает расстояние от начала
# дороги до i-го селения. В третьей строке входных данных
# задается число m - количество бомбоубежищ (1 <= m <= 100000).
# Четвертая строка содержит m различных целых чисел, i-е из
# этих чисел задает расстояние от начала дороги до i-го
# бомбоубежища. Все расстояния положительны и не превышают 10⁹.
# Селение и убежище могут располагаться в одной точке.
#
# Формат вывода
#
# Выведите n чисел - для каждого селения выведите номер
# ближайшего к нему бомбоубежища. Бомбоубежища пронумерованы
# от 1 до m в том порядке, в котором они заданы во входных данных.

import math as m


def sortDate(point):
    """Функция для сортировки данных по расстоянию"""
    return point[1]


def sortPosition(point):
    """Функция для сортировки данных по позиции"""
    return point[0]


#
# n - число домов
# houseList - расстояние от начала дороги до i-го селения
# m - число убежищ
# securityList - расстояние от начала дороги до i-го бомбоубежища.

n = int(input())
houseList = list(map(int, input().split()))
m = int(input())
securityList = list(map(int, input().split()))

# n = 10
# houseList = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
# m = 10
# securityList = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]

# Преобразование данных в кортеж
# houseListTuple - кортеж расстояния от начала дороги до селения
#   i - номер селения
# securityListTuple - кортеж расстояние от начала дороги до бомбоубежища
#   j - номер убежища

i = 1
j = 1
houseListTuple = []
securityListTuple = []
while i <= n:
    houseListTuple.append((i, houseList[i - 1]))
    i += 1

while j <= m:
    securityListTuple.append((j, securityList[j - 1]))
    j += 1

houseListTuple.sort(key=sortDate, reverse=True)
securityListTuple.sort(key=sortDate, reverse=True)

# Цикл для орпеделения результата
i = 0
j = 1
result = []
security = securityListTuple
house = houseListTuple

if m == 1:
    j = 0
    while i < n:
        result.append((house[i][0], security[j][0]))
        i += 1
else:
    while i < n:
        enter = True
        while enter and j < m:
            preExp = house[i][1] - security[(j - 1)][1]
            thisExp = house[i][1] - security[j][1]
            preExp = abs(preExp)
            thisExp = abs(thisExp)
            if preExp < thisExp:
                result.append((house[i][0], security[j - 1][0]))
                enter = False
            elif j == m - 1 and i < n:
                result.append((house[i][0], security[j][0]))
                enter = False
            else:
                j += 1
        i += 1

result.sort(key=sortPosition)
resultInp = []
for i in result:
    resultInp.append(i[1])

print(*resultInp)


# Цикл для определения близких расстояний по разнице для всего
# списка убежищ
# minLen - временный список для результатов разницы
# result - список для вывода результата
# num - разность расттояний между убежищем и селением
# i = 0
# result = []
# while i < n:
#    j = 0
#    minLen = []
#    while j < m:
#        if houseListTuple[i][1] - securityListTuple[j][1] < 0:
#            num = houseListTuple[i][1] - securityListTuple[j][1]
#            minLen.append((securityListTuple[j][0], -num))
#            j += 1
#        else:
#            num = houseListTuple[i][1] - securityListTuple[j][1]
#            minLen.append((securityListTuple[j][0], num))
#            j += 1
#    minLen.sort(key=sortDate)
#    result.append(minLen[0][0])
#    i += 1
#
# print(*result)
