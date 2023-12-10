import doctest
from uuid import uuid4, UUID


class Executor:
    def __init__(self, name: str):
        """
        Создание объекта "Исполнитель". 
        Является лицом, ответственным за проект. 
        У проекта может быть только один исполнитель.
        
        Подготовка объекта к работе:
        - генерация идентификатора

        :param name: Имя пользователя-исполнителя
        """
        self.id = uuid4()
        self.name = name

    def get_projects_id(self) -> list[UUID]:
        """
        Обращается к таблице проектов и по идентификатору исполнителя 
        находит проекты (записи), из id которых формируется список для возврата 

        :return: Список идентификаторов проектов исполнителя
        """
        ...
        
    def create_task(self, parent_id: UUID) -> None:
        """
        Создаёт задачу

        :param parent_id: Идентификатор старшей сущности задачи для привязки
        """
        ...

    def create_comment(self, project_id: UUID) -> None:
        """
        Создаёт комментарий проекта

        :param project_id: Идентификатор проекта для привязки комментария
        """
        ...


class Project:
    def __init__(self, title: str, deadline: str, executor_id: UUID):
        """
        Создание объекта "Проект"
        
        Подготовка проекта к работе:
        - генерация уникального идентификатора 
        - установка начального статуса

        :param title: Название проекта
        :param dedline: Крайний срок проекта (формат: "дд.мм.гггг")
        :param executor_id: Идентификатор ответственного за проект

        Примеры:
        >>> executor = Executor('Michail')
        >>> project_1 = Project('Купить хлеб', '21.10.2023', executor.id)  # инициализация экземпляра класса
        """
        self.id = uuid4()
        self.status = 'Новое'
        self.title = title
        self.deadline = deadline
        self.executor_id = executor_id

    def show_comments(self) -> None:
        """
        Отображение всех комментариев по проекту
        """
        ...

    def show_task_tree(self) -> None:
        """
        Отображение всех задач по проекту, включая подзадачи
        """
        ...

    def edit(self) -> None:
        """
        Переход к интерфейсу редактирования атрибутов проекта
        - названия
        - статуса
        - комментариев
        - задач
        - крайнего срока
        """
        ...


class Task:
    def __init__(self, title: str, parent_id: UUID):
        """
        Создание объекта "Задача"
        
        Подготовка объекта к работе:
        - генерация идентификатора 
        - установка начального статуса

        :param title: Формулировка задачи
        :param parent_id: Идентификатор старшей сущности (ей может быть проект или задача)

        Примеры:
        >>> executor = Executor('Michail')
        >>> project_1 = Project('Купить хлеб', '21.10.2023', executor.id)
        >>> task_1 = Task('task_A', project_1.id) 
        >>> task_2 = Task('task_B', project_1.id) 
        >>> task_3 = Task('task_C', project_1.id) 
        """
        self.id = uuid4()
        self.status = 'Новое'
        self.title = title
        self.parent_id = parent_id
        
    def edit(self) -> None:
        """
        Редактирование статуса и имени задачи
        """
        ...

    def add_subtask(self) -> None:
        """
        Добаление подзадачи
        """
        ...


class Comment:
    def __init__(self, text: str, project_id: UUID):
        """
        Создание объекта "Комментарий"
        
        Подготовка объекта к работе:
        - генерация идентификатора 
        - установка даты создания
        - привязка комментария к проекту
        - установка текста комментария

        :param project_id: Идентификатор проекта, к которому относится комментарий
        :param text: Текст комментария

        Примеры:
        >>> executor = Executor('Michail')
        >>> project_1 = Project('Купить хлеб', '21.10.2023', executor.id)
        >>> comment_1 = Comment('Comment_A_text', project_1.id) 
        >>> comment_2 = Comment('Comment_B_text', project_1.id) 
        """
        self.id = uuid4()
        self.text = text
        # self.date_of_creation = ... # Функция получения текущей даты из библиотеки datetime
        self.project_id = project_id

    def edit(self) -> None:
        """
        Редактирование комментария
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  
    