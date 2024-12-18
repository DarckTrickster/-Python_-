import doctest



class Tree:
    def init(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 20)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")
        self.age = age

    def grow(self, growth_rate: float) -> None:
        """
        Увеличение высоты дерева.

        :param growth_rate: Скорость роста дерева в метрах
        :raise ValueError: Если скорость роста отрицательная, вызывается ошибка

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 20)
        >>> tree.grow(0.5)
        """
        if not isinstance(growth_rate, (int, float)):
            raise TypeError("Скорость роста должна быть числом")
        if growth_rate < 0:
            raise ValueError("Скорость роста не может быть отрицательной")
        self.height += growth_rate

    def add_age(self, years: int) -> None:
        """
        Увеличение возраста дерева.

        :param years: Количество лет, которое нужно добавить
        :raise ValueError: Если количество лет отрицательное, вызывается ошибка

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 20)
        >>> tree.add_age(5)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным")
        self.age += years

    def is_mature(self) -> bool:
        """
        Проверка, является ли дерево зрелым (возраст > 50 лет).

        :return: True, если дерево зрелое, иначе False

        Примеры:
        >>> tree = Tree("Дуб", 15.5, 60)
        >>> tree.is_mature()
        True
        """
        return self.age > 50

class Stack:
    def init(self, max_size: int):
        """
        Создание и подготовка к работе объекта "Стек"

        :param max_size: Максимальный размер стека

        Примеры:
        >>> stack = Stack(10)  # инициализация экземпляра класса
        """
        if not isinstance(max_size, int):
            raise TypeError("Максимальный размер стека должен быть целым числом")
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть положительным числом")
        self.max_size = max_size
        self.items = []

    def push(self, item: object) -> None:
        """
        Добавление элемента в стек.

        :param item: Элемент, который нужно добавить
        :raise ValueError: Если стек переполнен, вызывается ошибка

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(1)
        >>> stack.push(2)
        """
        if len(self.items) >= self.max_size:
            raise ValueError("Стек переполнен")
        self.items.append(item)

    def pop(self) -> object:
        """
        Удаление и возврат верхнего элемента из стека.

        :raise ValueError: Если стек пуст, вызывается ошибка
        :return: Верхний элемент стека

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        """
        if not self.items:
            raise ValueError("Стек пуст")
        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Проверка, является ли стек пустым.

        :return: True, если стек пуст, иначе False

        Примеры:
        >>> stack = Stack(2)
        >>> stack.is_empty()
        True
        """
        return len(self.items) == 0


class Car:
    def init(self, brand: str, model: str, fuel_consumption: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param fuel_consumption: Расход топлива на 100 км

        Примеры:
        >>> car = Car("Toyota", "Corolla", 6.5)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not model:
            raise ValueError("Модель автомобиля не может быть пустой")
        self.model = model

        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть числом")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Расчет стоимости топлива для заданного расстояния.

        :param distance: Расстояние в километрах
        :param fuel_price: Цена топлива за литр
        :return: Стоимость топлива

        Примеры:
        >>> car = Car("Toyota", "Corolla", 6.5)
        >>> car.calculate_fuel_cost(200, 50)
        650.0
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть числом")
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        if not isinstance(fuel_price, (int, float)):
            raise TypeError("Цена топлива должна быть числом")
        if fuel_price < 0:
            raise ValueError("Цена топлива не может быть отрицательной")
        return (self.fuel_consumption / 100) * distance * fuel_price

    def is_economical(self) -> bool:
        """
        Проверка, является ли автомобиль экономичным (расход топлива < 7 л/100 км).

        :return: True, если автомобиль экономичный, иначе False

        Примеры:
        >>> car = Car("Toyota", "Corolla", 6.5)
        >>> car.is_economical()
        True
        """
        return self.fuel_consumption < 7



if __name__ == "__main__":
    doctest.testmod()
