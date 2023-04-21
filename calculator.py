# id решения в Яндекс.Контесте 86174799

class Stack:
    def __init__(self):
        self.__data = []

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        if not self.__data:
            return IndexError
        return self.__data.pop()


def calculate(input_string):
    dictionary = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }

    expression = Stack()
    for val in input_string:
        if val not in dictionary:
            expression.push(int(val))
        else:
            expression.push(dictionary[val](expression.pop(), expression.pop()))

    return expression.pop()


if __name__ == '__main__':
    print(calculate(input().split()))
