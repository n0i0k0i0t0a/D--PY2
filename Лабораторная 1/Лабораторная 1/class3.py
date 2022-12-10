import doctest


class Dictionary:
    def __init__(self, language_1, language_2, number_of_words):
        """
        Создание объекта и поготовка к работе
        :param language_1: язык, с которого переводят слова
        :param language_2: язык, на который переводят слова
        :param number_of_words: количество, переведенных слов
        Пример
        Dictionary('Немецкий', 'Русский', 1500)
        """
        if not isinstance(language_1, str):
            raise TypeError('Язык, с которого переводят слова должен быть записан строкой')
        self.language_1 = language_1
        if not isinstance(language_2, str):
            raise TypeError('Язык, с которого переводят слова должен быть записан строкой')
        self.language_2 = language_2
        if not isinstance(number_of_words, int):
            raise TypeError('Количество слов должно быть указано числом')
        if number_of_words < 0:
            raise ValueError('Количество переводимых слов не может быть меньше 0')
        self.number_of_words = number_of_words

    def write_new_word(self, word_1, word_2) -> int:
        """
        Метод добавляющий слова в словарь
        :param word_1: слово на немецком  языке
        :param word_2: слово на русском языке
        :return: количество слов в словаре
        Пример
        dict = Dictionary('Немецкий', 'Русский', 1500)
        dict.number_of_words += 1
        print(dict.number_of_words)
        """
        ...
    def delete_word(self, word_1, word_2) -> int:
        """
        Метод удаляющий слова из словаря
        :param word_1: слово на немецком языке
        :param word_2: слово на русском языке
        :return: количество слов в словаре
        Пример
        dict = Dictionary('Немецкий', 'Русский', 1501)
        dict.number_of_words -= 1
        print(dict.number_of_words)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

