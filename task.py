class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.set_pages(pages)

    def get_pages(self):
        return self.__pages

    def set_pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.__pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.get_pages()!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.set_duration(duration)

    def get_duration(self):
        return self.__duration

    def set_duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.__duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, duration={self.get_duration()!r})"


BOOK_DATABASE = [
    PaperBook(name="Война и мир", author="Лев Толстой", pages=1225),
    AudioBook(name="1984", author="Джордж Оруэлл", duration=11.5),
    PaperBook(name="Мастер и Маргарита", author="Михаил Булгаков", pages=480),
    AudioBook(name="Гарри Поттер и философский камень", author="Джоан Роулинг", duration=8.5)
]


for book in BOOK_DATABASE:
    print(str(book))
    print(repr(book))
    print()
