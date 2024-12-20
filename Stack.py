#Stack is a data structure that the order of data together obeys the rule "Last is, First out". In simple words, the latest added element is the first element to be removed.

class Stack:
    def __init__(self, limit = 100):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) ==0
    
    def is_full(self):
        return len(self.stack) == self.limit
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
            
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        else:
            return self.stack[-1]
        
    def push(self, data):
        if self.is_full():
            print("Stack is full")
            return -1
        else:
            self.stack.append(data)

    
    def show(self):
        if self.is_empty():
            print("Stack is empty")

            return -1
        else:
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])


    def replace(self, x, y):
        if self.is_empty():
            print("Stack is empty")
            return -1
        temp = []
        i = 0
        while not self.is_empty():
            temp.append(self.pop())
            if temp[i] == x:
                temp[i] = y
            i +=1
        while len(temp) > 0:
            self.push(temp.pop())

