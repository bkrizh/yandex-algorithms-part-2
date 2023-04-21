# id решения в Яндекс.Контесте 86174741

class OverflowList(Exception):
    """Нет места для добавления элемента в список, он заполнен на всю длину"""
    pass


class EmptyList(Exception):
    """Нечего извлекать из списка, он не содержит элементов"""
    pass


class MyQueue:

    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_sized = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def calculation_index(self, value):
        return value % self.__max_sized

    def check_size(self):
        return self.__size == self.__max_sized

    def check_empty(self):
        return self.__size == 0

    def push_back(self, x):
        if self.check_size():
            raise OverflowList
        self.__queue[self.__tail] = x
        self.__tail = self.calculation_index(self.__tail+1)
        self.__size += 1

    def pop_front(self):
        if self.check_empty():
            raise EmptyList
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.calculation_index(self.__head+1)
        self.__size -= 1
        return x

    def push_front(self, x):
        if self.check_size():
            raise OverflowList
        self.__queue[self.__head - 1] = x
        self.__head = self.calculation_index(self.__head-1)
        self.__size += 1

    def pop_back(self):
        if self.check_empty():
            raise EmptyList
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self.calculation_index(self.__tail-1)
        self.__size -= 1
        return x


if __name__ == '__main__':
    quantity_commands = int(input())
    queue_size = int(input())
    queue = MyQueue(queue_size)
    for i in range(quantity_commands):
        commands = input()
        command, *args = commands.split()
        action = getattr(MyQueue, command)
        try:
            print(action(queue)) if not args else action(queue, args[0])
        except (OverflowList, EmptyList):
            print('error')
