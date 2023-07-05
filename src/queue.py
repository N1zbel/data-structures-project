class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Возвращает итератор для очереди

        :return: итератор для очереди
        """
        current = self.head
        while current is not None:
            yield current.data
            current = current.next_node

    def __str__(self):
        new_queue = []
        for item in self:
            new_queue.append(item)
        return '\n'.join(new_queue)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.tail is None:
            return None

        data = self.head.data
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None

        return data
