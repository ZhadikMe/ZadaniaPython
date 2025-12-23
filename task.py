class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор базового класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строковое представление автомобиля.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление автомобиля.

        :return: Официальное строковое представление автомобиля.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return "Двигатель запущен."

class PassengerCar(Car):
    def __init__(self, brand: str, model: str, year: int, num_seats: int):
        """
        Конструктор дочернего класса PassengerCar.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param num_seats: Количество мест в автомобиле.
        """
        super().__init__(brand, model, year)
        self.num_seats = num_seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строковое представление легкового автомобиля.
        """
        return f"{self.year} {self.brand} {self.model} с {self.num_seats} сиденьями"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление легкового автомобиля.

        :return: Официальное строковое представление легкового автомобиля.
        """
        return f"PassengerCar(brand='{self.brand}', model='{self.model}', year={self.year}, num_seats={self.num_seats})"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового(!) автомобиля с указанием количества мест.

        :return: Сообщение о запуске двигателя легкового автомобиля.
        """
        return f"Двигатель пассажирского автомобиля с {self.num_seats} сидениями запущен"

    def open_trunk(self) -> str:
        """
        Открывает багажник легкового автомобиля.

        :return: Сообщение об открытии багажника.
        """
        return "Багажник открыт."

class Truck(Car):
    def __init__(self, brand: str, model: str, year: int, load_capacity: float):
        """
        Конструктор дочернего класса Truck.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param load_capacity: Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строковое представление грузового автомобиля.
        """
        return f"{self.year} {self.brand} {self.model} с {self.load_capacity} тоннами грузоподъемности"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление грузового автомобиля.

        :return: Официальное строковое представление грузового автомобиля.
        """
        return f"Truck(brand='{self.brand}', model='{self.model}', year={self.year}, load_capacity={self.load_capacity})"

    def start_engine(self) -> str:
        """
        Запускает двигатель грузового(!) автомобиля с указанием грузоподъемности.

        :return: Сообщение о запуске двигателя грузового автомобиля.
        """
        return f"Двигатель грузового автомобиля с грузоподъемностью {self.load_capacity}."

    def load_cargo(self, weight: float) -> str:
        """
        Загружает груз в грузовой автомобиль.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке груза.
        """
        if weight > self.load_capacity:
            return "Груз превышает грузоподъемность."
        return f"Груз весом {weight} тон загружен."


if __name__ == "__main__":
    # Пример использования классов
    passenger_car = PassengerCar("Toyota", "Corolla", 2020, 5)
    truck = Truck("Volvo", "FH16", 2019, 20)

    print(passenger_car)
    print(passenger_car.start_engine())
    print(passenger_car.open_trunk())

    print(truck)
    print(truck.start_engine())
    print(truck.load_cargo(15))
    print(truck.load_cargo(25))

