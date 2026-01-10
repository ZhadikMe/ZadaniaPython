# __init__.py

class Book:
    def __init__(self, title: str, pages: int, summary: str):
        if not isinstance(title, str) or not title:
            raise ValueError("Название должно быть непустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        if not isinstance(summary, str) or not summary:
            raise ValueError("Краткое содержание должно быть непустой строкой.")

        self.title = title
        self.pages = pages
        self.summary = summary

    def read(self, page_number: int) -> str:
        """
        Прочитать определенную страницу книги.

        Аргументы:
            page_number (int): Номер страницы для чтения.

        Возвращает:
            str: Содержимое указанной страницы.

        >>> book = Book("Пример книги", 100, "Это пример краткого содержания.")
        >>> book.read(1)
        'Содержимое страницы 1'
        """
        return f'Содержимое страницы {page_number}'

    def get_summary(self) -> str:
        """
        Получить краткое содержание книги.

        Возвращает:
            str: Краткое содержание книги.

        >>> book = Book("Пример книги", 100, "Это пример краткого содержания.")
        >>> book.get_summary()
        'Это пример краткого содержания.'
        """
        return self.summary

class Car:
    def __init__(self, brand: str, horsepower: int):
        if not isinstance(brand, str) or not brand:
            raise ValueError("Марка должна быть непустой строкой.")
        if not isinstance(horsepower, int) or horsepower <= 0:
            raise ValueError("Лошадиные силы должны быть положительным целым числом.")

        self.brand = brand
        self.horsepower = horsepower

    def start_engine(self) -> None:
        """
        Запустить двигатель автомобиля.

        >>> car = Car("Lada", 120)
        >>> car.start_engine()
        None
        """


    def drive(self, distance: float) -> float:
        """
        Проехать на автомобиле указанное расстояние.

        Аргументы:
            distance (float): Расстояние для поездки в километрах.

        >>> car = Car("Lada", 120)
        >>> car.drive(100.0)
        None
        """
        return f'Проехали {distance} км.'

class Website:
    def __init__(self, url: str, domain: str):
        if not isinstance(url, str) or not url:
            raise ValueError("URL должен быть непустой строкой.")
        if not isinstance(domain, str) or not domain:
            raise ValueError("Домен должен быть непустой строкой.")

        self.url = url
        self.domain = domain

    def visit(self) -> str:
        """
        Получить ссылку на веб-сайт.

        >>> website = Website("https://example.com", "example.com")
        >>> website.visit()
        'Посетить веб-сайт https://example.com.'
        """
        return f'Посетить веб-сайт {self.url}.'

    def get_page_content(self, path: str) -> str:
        """
        Получить содержимое определенной страницы на веб-сайте.

        Аргументы:
            path (str): Путь к странице.

        Возвращает:
            str: Содержимое указанной страницы.

        >>> website = Website("https://example.com", "example.com")
        >>> website.get_page_content("/about")
        'Это страница "О нас". Здесь вы можете узнать больше о нашей компании.'
        """
        return f'Страница {path} не найдена.'

# Инициализация объектов
book = Book("Пример книги", 100, "Это пример краткого содержания.")
car = Car("Toyota", 150)
website = Website("https://example.com", "example.com")
