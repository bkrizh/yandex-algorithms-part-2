# id решения в Яндекс.Контесте 86061966

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) == 0:
            return 'error'
        else:
            return self.data.pop()


def calculate(input_string):
    dictionary = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y//x
    }

    expression = Stack()
    for val in input_string:
        if val not in ['+', '-', '*', '/']:
            expression.push(int(val))
        else:
            expression.push(dictionary[val](expression.pop(), expression.pop()))

    return expression.pop()


print(calculate(input().split()))
