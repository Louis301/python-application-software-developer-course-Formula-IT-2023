class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self) -> str:
        """ Вывод человекочитаемой информации об экземпляре """
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        """ Вывод вывод технической информации об экземпляре """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def author(self) -> str:
        return self._author
    

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """ Создание экземпляра бумажной книги """
        super().__init__(name, author)
        self.pages = pages

    def __str__(self) -> str:
        """ Переопределённый метод __str__ базового класса Book c применением наследования """
        return f"{super().__str__()}. Число страниц {self._pages}"
    
    def __repr__(self):
        """ Переопределённый метод __repr__ базового класса Book """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self) -> int:
        return self._pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        if isinstance(pages, int):
            if pages > 0:   
                self._pages = pages
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть целочисленного типа')


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """ Создание экземпляра аудиокниги """
        super().__init__(name, author)
        self.duration = duration
    
    def __str__(self):
        """ Переопределённый метод __str__ базового класса Book c применением наследования """
        return f"{super().__str__()}. Продолжительность {self._duration}"
    
    def __repr__(self):
        """ Переопределённый метод __repr__ базового класса Book """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
    
    @property
    def duration(self) -> float:
        return self._duration
    
    @duration.setter
    def duration(self, duration: float) -> None:
        if isinstance(duration, float):
            if duration > 0:   
                self._duration = duration
            else:
                raise ValueError('Аргумент меньше или равен нулю')
        else:
            raise TypeError('Аргумент должен быть вещественного типа')
    