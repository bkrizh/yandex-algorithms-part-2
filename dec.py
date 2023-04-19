# id решения в Яндекс.Контесте 86015569

class MyQueue:

    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_sized = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, x):
        if self.size != self.max_sized:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_sized
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.size != 0:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_sized
            self.size -= 1
            print(x)
        else:
            print('error')

    def push_front(self, x):
        if self.size != self.max_sized:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_sized
            self.size += 1
        else:
            print('error')

    def pop_back(self):
        if self.size != 0:
            x = self.queue[self.tail - 1]
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_sized
            self.size -= 1
            print(x)
        else:
            print('error')


quantity_commands = int(input())
queue_size = int(input())
queue = MyQueue(queue_size)

for i in range(quantity_commands):
    command = input().split()
    if command[0] == 'push_back':
        queue.push_back(int(command[1]))
    elif command[0] == 'push_front':
        queue.push_front(int(command[1]))
    elif command[0] == 'pop_front':
        queue.pop_front()
    else:
        queue.pop_back()
