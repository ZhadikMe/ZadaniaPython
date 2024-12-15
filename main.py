# main.py

from __init__ import book, car, website

def main():
    # Пример использования класса Book
    print(book.get_summary())
    print(book.)

    # Пример использования класса Car
    print(car.start_engine())
    print(car.drive(100.0))

    # Пример использования класса Website
    print(website.visit())
    print(website.get_page_content("/about"))

if __name__ == "__main__":
    main()
