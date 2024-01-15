class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Создание объекта "Книга"
                
        :param id: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает характеристику объекта в виде строки

        :return: Строка, содержащая название книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр Book, идентичный настоящему

        :return: Команда вызова конструктора Book
        """
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Создание объекта "Библиотека"

        Атрибут books инициализируется пустым списком, если аргумент параметра books не указан
                
        :param books: Список идентификаторов книг (необязательный)
        """
        self.books = [] if books is None else books 

    def get_next_book_id(self) -> int:
        """
        Возвращает индекс книги для добавления в список Books

        :return: единица, если список books пустой, иначе - значение последнего элемента списка идентификаторов, увеличенное на единицу
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1] + 1

    def get_index_by_book_id(self, id: int) -> int:
        """
        Возвращает индекс элемента списка books, равного запрошенному идентификатору книги (id)
                
        :param id: Идентификатор книги

        :return: Индекс элемента id в списке. Если такого элемента нет - генерируем исключение ValueError
        """
        for index, book_id in enumerate(self.books):
            if id == book_id:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")
