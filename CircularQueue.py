class CircularQueue:
    def __init__(self, limit=100):
        self.cQ = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.limit == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Circular queue is full")
            return -1
        elif self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.limit
        self.cQ[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Circular queue is empty")
            return -1
        elif self.front == self.rear:
            data = self.cQ[self.front]
            self.front = -1
            self.rear = -1
            return data
        else:
            data = self.cQ[self.front]
            self.front = (self.front + 1) % self.limit
            return data

    def display(self):
        if self.is_empty():
            print("Circular queue is empty")
            return -1
        print("Circular Queue: ")
        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.cQ[i], end=" ")
        else:
            for i in range(self.front, self.limit):
                print(self.cQ[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.cQ[i], end=" ")
        print()


#Reversing a string with the use of Circular Queue
def reverse_string(string):
    queue = CircularQueue(len(string))
    for char in string:
        queue.enqueue(char)

    reversed_format = ""
    while not queue.is_empty():
        reversed_format = queue.dequeue() + reversed_format

    return reversed_format



