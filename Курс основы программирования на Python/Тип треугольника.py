# Курс основы программирования на Python
# Задание по программированию: Тип треугольника
# 14.04.2019
#
# Даны три стороны треугольника a,b,c. Определите тип треугольника с
# заданными сторонами. Выведите одно из четырех слов: rectangular для
# прямоугольного треугольника, acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или impossible, если треугольника
# с такими сторонами не существует (считаем, что вырожденный треугольник тоже невозможен).
#
# Формат ввода
#
# Вводятся три целых числа.
#
# Формат вывода
#
# Выведите ответ на задачу.

a = int(input())
b = int(input())
c = int(input())

if a == b + c or b == a + c or c == a + b:
    print('impossible')
elif (a == b and c > a) or (c == b and a > c) or (a == c and b > a):
    print('impossible')
elif a == 0 or b == 0 or c == 0:
    print('impossible')
elif a > b and a > c:
    if a**2 == c**2 + b**2:
        print('rectangular')
    elif a**2 < c**2 + b**2:
        print('acute')
    elif a**2 > c**2 + b**2:
        print('obtuse')
elif b > a and b > c:
    if b**2 == c**2 + a**2:
        print('rectangular')
    elif b**2 < c**2 + a**2:
        print('acute')
    elif b**2 > c**2 + a**2:
        print('obtuse')
elif c > b and c > a:
    if c**2 == a**2 + b**2:
        print('rectangular')
    elif c**2 < a**2 + b**2:
        print('acute')
    elif c**2 > a**2 + b**2:
        print('obtuse')
elif a == b and a == c:
    print('acute')
elif (a == b and c < a) or (c == b and a < c) or (a == c and b < a):
    print('acute')
