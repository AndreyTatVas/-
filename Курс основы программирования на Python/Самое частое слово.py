# Курс основы программирования на Python
# Задание по программированию: Самое частое слово
# 21.05.2019
#
# Дан текст. Выведите слово, которое в этом тексте
# встречается чаще всего. Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.
#
# Формат ввода
#
# Вводится текст.
#
# Формат вывода
#
# Выведите ответ на задачу.
#
# inFile - файл с исходными значениями
# onFile - файл с результатами
# wordCountDict - словарь содержащий количество упоминаний слова
#
inFile = open('input.txt')
onFile = open('output.txt', 'w', encoding='utf8')
wordCountDict = {}
for string in inFile:
    for word in list(string.split()):
        wordCountDict[word] = wordCountDict.get(word, 0) + 1
maxNum = 0
for key in sorted(wordCountDict):
    if wordCountDict[key] > maxNum:
        maxNum = wordCountDict[key]
        result = key
print(result, file=onFile)

inFile.close()
onFile.close()
