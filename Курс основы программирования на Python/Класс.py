# Курс основы программирования на Python
# Задание по программированию: Класс
# 27.05.2019
#
# Реализуйте класс Matrix. Он должен содержать:
#
# Конструктор от списка списков. Гарантируется, что списки
# состоят из чисел, не пусты и все имеют одинаковый размер.
# Конструктор должен копировать содержимое списка списков,
# т. е. при изменении списков, от которых была сконструирована
# матрица, содержимое матрицы изменяться не должно.
#
# Метод __str__, переводящий матрицу в строку. При этом элементы
# внутри одной строки должны быть разделены знаками табуляции,
# а строки — переносами строк. После каждой строки не должно
# быть символа табуляции и в конце не должно быть переноса строки.
# Метод size без аргументов, возвращающий кортеж вида (число строк,
# число столбцов). Пример теста с участием этого метода есть в
# следующей задаче этой недели.
#
# Добавьте в предыдущий класс следующие методы:
#
# __add__, принимающий вторую матрицу того же размера и возвращающий
# сумму матриц.
# __mul__, принимающий число типа int или float и возвращающий матрицу,
# умноженную на скаляр.
# __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван
# в том случае, аргумент находится справа. Для реализации этого метода в
# коде класса достаточно написать __rmul__ = __mul__.
# Формат ввода
#
# Вводится исходный код тестирующей программы на языке Python.
#
# Формат вывода
#
# Выведите результат её работы в текущем окружении при помощи exec,
# как это указано в условии.
#
from sys import stdin


class MatrixError(BaseException):
    """Класс ошибок для матриц"""
    def __init__(self, arg1, arg2):
        self.matrix1 = arg1
        self.matrix2 = arg2


class Matrix:
    def __init__(self, values):
        """Инициализирует атрибуты values"""
        self.values = list(values)

    def __str__(self):
        """Вывод при использовании метода str"""
        result = str()
        for i in self.values:
            for now in i:
                result += str(now) + '\t'
            result = result.rstrip()
            result += '\n'
        result = result.rstrip()
        return str(result)

    def size(self):
        """Выводит размер матрицы"""
        line = len(self.values)
        column = len(self.values[0])
        return (line, column)

    def __add__(self, other):
        """Сложение матриц"""
        if len(self.values) == len(other.values):
            result = []
            i = 0
            while i < len(self.values):
                j = 0
                line = []
                while j < len(self.values[0]):
                    line.append(self.values[i][j] + other.values[i][j])
                    j += 1
                result.append(line)
                i += 1
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    def __mul__(self, other):
        """Умножение матрицы на скаляр"""
        if isinstance(other, int) or isinstance(other, float):
            result = []
            i = 0
            while i < len(self.values):
                j = 0
                line = []
                while j < len(self.values):
                    line.append(self.values[i][j] * other)
                    j += 1
                result.append(line)
                i += 1
            return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        """Транспонирование матрицы"""
        result = []
        i = 0
        while i < len(self.values[0]):
            line = []
            j = 0
            while j < len(self.values):
                line.append(self.values[j][i])
                j += 1
            i += 1
            result.append(line)
        self.values = result
        return Matrix(result)

    def transposed(self):
        """Метод возвращающий транспонированную матрицу"""
        result = []
        i = 0
        while i < len(self.values[0]):
            line = []
            j = 0
            while j < len(self.values):
                line.append(self.values[j][i])
                j += 1
            i += 1
            result.append(line)
        return Matrix(result)


exec(stdin.read())
