# Курс основы программирования на Python
# Задание по программированию: Полиглоты
# 20.05.2019
#
# Каждый из N школьников некоторой школы знает Mᵢ
# языков. Определите, какие языки знают все школьники
# и языки, которые знает хотя бы один из школьников.
#
# Формат ввода
#
# Первая строка входных данных содержит количество
# школьников N. Далее идет N чисел Mᵢ, после каждого
# из чисел идет Mᵢ строк, содержащих названия языков,
# которые знает i-й школьник. Длина названий языков
# не превышает 1000 символов, количество различных
# языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.
#
# Формат вывода
#
# В первой строке выведите количество языков, которые
# знают все школьники. Начиная со второй строки -
# список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих
# строках - список таких языков.
#
# inFile - Файл с исходными данными
# onFile - Файл с конечнымии данными
# schCount - число учеников
# langCount - число языков для iго ученика
# schLangInfo - общая информация об языках
# langInfoSet - названия языков для iго ученика
# oneSch - языки, которые знает 1 ученик
# allSch - языки, которые знают все ученики
inFile = open('input.txt', 'r', encoding='utf8')
onFile = open('output.txt', 'w', encoding='utf8')
schLangInfo = []
schCount = int(inFile.readline())
i = 1
while i <= schCount:  # Цикл по всем ученикам
    langInfoSet = set()
    langCount = int(inFile.readline())
    j = 1
    while j <= langCount:  # Цикл для считывания всех
        # языков для iго ученика
        for language in inFile.readline().split():
            langInfoSet.add(language)
        j += 1
    schLangInfo.append(langInfoSet)
    i += 1

schLangInfo.sort()  # Сортировка, чтобы идти от большего
# множества к меньшему


allSch = set()
oneSch = set(schLangInfo[len(schLangInfo) - 1])  # присваиваем
# переменной большее множество
for langSet in range(len(schLangInfo) - 1, -1, -1):
    allSch |= schLangInfo[langSet]
    oneSch &= schLangInfo[langSet]

# Преобразовываем множества в список с дальнейшей
# сортировкой. Это необходимо, чтобы вывод значений
# был отсортирован и не менялся
oneSch = list(oneSch)
allSch = list(allSch)
oneSch.sort(reverse=True)
allSch.sort(reverse=True)

print(len(oneSch), file=onFile)
for name in oneSch:
    print(name, file=onFile)
print(len(allSch), file=onFile)
for name in allSch:
    print(name, file=onFile)

onFile.close()
inFile.close()
