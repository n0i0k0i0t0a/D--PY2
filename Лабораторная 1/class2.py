import doctest


class Ruler:
    def __init__(self, long: (int, float), material: str):
        """
        Создание объекта и подготовка к работе
        :param long: Длина линейки
        :param material: Материал, из которого линейка изготовлена
        Пример
        Ruler(25, 'metal') # инициализация экземпляра класса
        """
        self.long = long
        self.material = material

    def drow(self, point_1, point_2) -> int:
        """
        :param point_1: Точка, от которой нужно начать чертить
        :param point_2: Точка, к которой нужно провести линию
        :return: Длина отрезка между двумя точками
        Пример
        ruler = Ruler(25, 'metal')
        ruler.drow((0;0), (1,1))
        """
        if not isinstance(point_1, (float,float)):
            raise TypeError('Значения точки должны задаваться двумя координатами')
        if not isinstance(point_2, (float, float)):
            raise TypeError('Значения точки должны задаваться двумя координатами')
        ...

    def measure(self, point_1, point_2) -> int:
        """
        :param point_1: Точка, от которой нужно начать отмерять
        :param point_2: Точка, до которой нужно отмерить расстояние
        :return: Расстояние между точками в виде числа
        Пример
        ruler = Ruler(25, 'metal')
        ruler.measure((4, 8),(-5, 1))
        """
        if not isinstance(point_1, (float,float)):
            raise TypeError('Значения точки должны задаваться двумя координатами')
        if not isinstance(point_2, (float, float)):
            raise TypeError('Значения точки должны задаваться двумя координатами')
        ...


if __name__ == "__main__":
    doctest.testmod()


