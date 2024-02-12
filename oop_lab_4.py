import math


class Shape:
    def __init__(self, name: str):
        """ Создание экземпляра базового класса геометрических фигур """
        self._name = name

    def __str__(self) -> str:
        """ Вывод человекочитаемой информации о фигуре """
        return f'Имя: {self._name}'

    def __repr__(self) -> str:
        """ Вывод технической информации о фигуре """
        return f"{self.__class__.__name__}(name={self._name!r})"


class Circle(Shape):
    def __init__(self, name: str, radius: int):
        """ Создание экземпляра класса 'Окружность' с наследованием конструктора базового класса фигур """
        super().__init__(name)
        self.radius = radius

    @property
    def radius(self) -> int:
        return self._radius
    
    @radius.setter
    def radius(self, radius: int) -> None:
        if isinstance(radius, int):
            if radius > 0:   
                self._radius = radius
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')

    def __str__(self) -> str:
        """ Переопределённый метод __str__ базового класса фигур c применением наследования """
        return f"{super().__str__()}, Радиус: {self._radius}"
    
    def __repr__(self) -> str:
        """ Переопределённый метод __repr__ базового класса 'Фигура' """
        return f"{self.__class__.__name__}(name={self._name!r}, radius={self._radius!r})"

    def get_area(self) -> float:
        """ Вычисление площади круга и возврат полученного значения """
        return math.pi * (self._radius ** 2)


class Squire(Shape):
    def __init__(self, name: str, width: int):
        """ Создание экземпляра класса 'Квадрат' с наследованием конструктора базового класса 'Фигура' """
        super().__init__(name)
        self.width = width

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, width: int) -> None:
        if isinstance(width, int):
            if width > 0:   
                self._width = width
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')
    
    def __str__(self) -> str:
        """ Переопределённый метод __str__ базового класса фигур c применением наследования """
        return f"{super().__str__()}, Сторона: {self._width}"
    
    def __repr__(self) -> str:
        """ Переопределённый метод __repr__ базового класса 'Фигура' """
        return f"{self.__class__.__name__}(name={self._name!r}, width={self._width!r})"

    def get_area(self) -> int:
        """ Вычисление площади квадрата и возврат полученного значения """
        return self._width ** 2
    

class Rectangle(Squire):
    def __init__(self, name: str, width: int, height: int):
        """ Создание экземпляра класса 'Прямоугольник' с наследованием конструктора базового класса 'Квадрат' """
        super().__init__(name, width)
        self.height = height
        
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, height: int) -> None:
        if isinstance(height, int):
            if height > 0:   
                self._height = height
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')

    def __str__(self) -> str:
        """ Переопределённый метод __str__ базового класса 'Квадрат' c применением наследования """
        return f"{super().__str__()}, Ширина: {self._width}, Высота: {self._height}"

    def __repr__(self) -> str:
        """ Переопределённый метод __repr__ базового класса 'Квадрат' """
        return f"{self.__class__.__name__}(name={self._name!r}, width={self._width!r}, height={self._height!r})"

    def get_area(self) -> int:
        """ Переопределённый метод базового класса для вычисления площади прямоугольника """
        return self._width * self._height
    