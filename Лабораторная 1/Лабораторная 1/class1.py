import doctest


class NoteBook:
    def __init__(self, pages: int, appearance: str, sheets: str):

        """"
        Создание объекта и подготовка к работе
        :param pages: количество страниц
        :param appearence: внешний вид тетради (блокового типа, на гребне, на скрепке)
        :param sheets: как выглядят листы тетради (в клетку, линейку, ромбик,...)
        Пример
        NoteBook(96, гребень, клетка) # инициализация экземпляра класса
        """

        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно представлять собой целое число')
        if pages < 0:
            raise ValueError('Количество листов должно быть положительным')
        self.pages = pages
        if not isinstance(appearance, str):
            raise TypeError('Внешний вид тетради должен быть описан словом')
        self.appearance = appearance
        if not isinstance(sheets, str):
            raise TypeError('Тип листов должен быть описан словом')
        self.sheets = sheets

    def tear_out(self, page, pages) -> int:
        """
        Метод описывающий процесс вырывания листов из тетради
        :param page: Количество вырванных листов
        :param pages: Количество листов в тетради
        :return: Количество оставшихся листов в тетради
        Пример
        note = NoteBook(96, 'гребень', 'клетка')
        note.tear_out(48)
        """
        if not isinstance(page, int):
            raise TypeError('Количество вырванных листов должно быть числом')
        if not isinstance(page, int):
            raise ValueError('Количество вырванных листов должно быть целым числом')
        if not isinstance(pages, int):
            raise TypeError('Количество вырванных листов должно быть числом')
        if not isinstance(pages, int):
            raise ValueError('Количество вырванных листов должно быть целым числом')
        if page > pages:
            raise ValueError('Количество вырываемых листов не должно превышать количество листов в тетради')
        ...

    def write(self, symbol) -> str:
        """
        :param symbol: Символ записанный в тетрадь
        :return: все символы, которые до этого были записаны в тетрадь
        Пример
        note = NoteBook(96, 'гребень', 'клетка')
        note.write('S')
        """
        if not isinstance(symbol, str):
            raise TypeError('Записываемый символ должен быть формата строки')
        if len(symbol) > 1:
            raise ValueError('Количество записываемых за раз символов не должно превышать 1')
        ...


if __name__ == "__main__":
    doctest.testmod()


