class dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class Dlinkedlist:
    def __init__(self):
        self.head = None

    def ins_first(self, data):
        n = dnode(data)
        if self.head is None:
            self.head = n
            return
        n.next = self.head
        self.head.back = n
        self.head = n

    def ins_last(self, data):
        n = dnode(data)
        if self.head is None:
            self.head = n
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.back = temp

    def ins_after(self, X, data):
        if self.head is None:
            return
        temp = self.head
        while temp.data != X:
            if temp.next is None:
                return
            temp = temp.next
        n = dnode(data)
        n.next = temp.next
        if temp.next:  # Ensure temp.next is not None
            temp.next.back = n
        temp.next = n
        n.back = temp

    def del_first(self):
        if self.head is None:
            return
        if self.head.next is None:  # If only one node exists
            self.head = None
            return
        self.head = self.head.next
        self.head.back = None

    def del_last(self):
        if self.head is None:
            return
        if self.head.next is None:  # If only one node exists
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def del_after(self, X):
        if self.head is None or self.head.next is None:
            return
        temp = self.head
        while temp.data != X:
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            if temp.next.next:  # Ensure temp.next.next is not None
                temp.next.next.back = temp
            temp.next = temp.next.next

    def delete(self, X):
        if self.head is None:
            return
        if self.head.data == X:
            if self.head.next:
                self.head = self.head.next
                self.head.back = None
                return
            else:  # Only one node
                self.head = None
                return
        temp = self.head
        while temp.data != X:
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            temp.next.back = temp.back
            temp.back.next = temp.next
        else:
            temp.back.next = None

    def display(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.data, end=" <-> ")
            else:
                print(temp.data)
            temp = temp.next

