#Max Heap is a data structure retrieved from tree concepts that parent node is always larger than its children. we always keep it like that by calling the method "heapify" which controls whether the parent is larger or not.


class max_heap:
    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)
        self.heapify(len(self.list) - 1)

    def heapify(self, n):
        p = (n - 1) // 2 
        if p >= 0:
            if self.list[p] < self.list[n]:
                self.list[p], self.list[n] = self.list[n], self.list[p]
                self.heapify(p)

    def del_root(self):
        L = len(self.list)
        if L == 0:
            return 
        self.list[0], self.list[L - 1] = self.list[L - 1], self.list[0]
        self.list.pop() 
        self.heapifyud(0) 

    def heapifyud(self, n):
        L = len(self.list)
        Left = 2 * n + 1
        Right = 2 * n + 2
        largest = n

        if Left < L and self.list[Left] > self.list[largest]:
            largest = Left
        if Right < L and self.list[Right] > self.list[largest]:
            largest = Right

        if largest != n:
            self.list[n], self.list[largest] = self.list[largest], self.list[n]
            self.heapifyud(largest)



    def delete(self, data):
        try:
            index = self.list.index(data) 
            L = len(self.list)
            if index == L - 1: 
                self.list.pop()
            else:

                self.list[index], self.list[L - 1] = self.list[L - 1], self.list[index]
                self.list.pop()
    
                self.heapify(index) 
                self.heapifyud(index)
        except ValueError:
            print("Element not found in the heap")
