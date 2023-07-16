# Курс основы программирования на Python
# Задание по программированию: Сократите дробь
# 08.05.2019
#
# Даны два натуральных числа n и m.
#
# Сократите дробь (n / m), то есть выведите два других числа p и q
# таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
#
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения
# n и m и возвращающей кортеж из двух чисел: return p, q.
#
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
#
# Формат ввода
#
# Вводятся два натуральных числа.
#
# Формат вывода
#
# Выведите ответ на задачу.

def gcd(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    if a < b:
        result = gcd(a, b % a)
    else:
        result = gcd(a % b, b)
    return result


def ReduceFraction(n, m):
    nod = gcd(n, m)
    n = n // nod
    m = m // nod
    return n, m


n, m = int(input()), int(input())
n, m = ReduceFraction(n, m)
print(n, m)
