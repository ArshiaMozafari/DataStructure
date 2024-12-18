
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ins_first(self, data):
        a = Node(data)
        a.next = self.head
        self.head = a

    def ins_last(self, data):
        a = Node(data)
        if self.head is None:
            self.head = a
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a

    def ins_next(self, x, data):
        n = Node(data)
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            if temp.data == x:
                n.next = temp.next
                temp.next = n
                return
            temp = temp.next
        print("Node with data", x, "not found")

    def del_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def del_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def del_next(self, x):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        if temp and temp.next:
            temp.next = temp.next.next
        else:
            print("Node with data", x, "not found or it has no next node")


    def delete(self, x):
        if self.head is None:
            print("Empty")
            return
        if self.head.data == x:
            if self.head.next is None:
                a = self.head
                self.head = None
                del a
                return
            a = self.head
            self.head = self.head.next
            del a
            return
        temp = self.head
        while temp.next.data != x:
            if temp.next is None:
                print(f"{x} was not found")
                return
            temp = temp.next
        a = temp.next
        temp.next = temp.next.next
        del a

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")
