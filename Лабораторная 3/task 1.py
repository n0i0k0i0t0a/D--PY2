class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    'Дочерний класс книги'
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # вызываем конструктор базового класса
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Количество страниц: {self._pages}"


class AudioBook(Book):
    'Дочерний класс книги'
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # вызываем конструктор базового класса
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность прослушивания книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность прослушивания должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность прослушивания должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность прослушивания:{self._duration}"


audio = AudioBook('Евгений Онегин', 'A.C.Пушкин', 5.0)
print(audio)


