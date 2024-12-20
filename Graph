#Undirected simple graph with BFS show

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

class Graph:
    def __init__(self, n):
        self.M = [[0] * n for i in range(n)]

    def ins_edge(self, s, t):
        self.M[s][t] = 1
        self.M[t][s] = 1

    def del_edge(self, s, t):
        self.M[s][t] = 0
        self.M[t][s] = 0

    def degree(self, A):
        return sum(self.M[A])
    
    def bfs_show(self, start):
        n = len(self.M)
        temp = [False] * n
        queue = CircularQueue(n)

        queue.enqueue(start)
        temp[start] = True

        bfs_list = []
        while not queue.is_empty():
            node = queue.dequeue()
            bfs_list.append(node)

            for i in range(n):
                if self.M[node][i] == 1 and not temp[i]:
                    queue.enqueue(i)
                    temp[i] = True
        print(bfs_list)


    def modify_V(self, add=True, index=0):
        n = len(self.M)
        if add:
            for i in range(n):
                self.M[i].insert(index, 0)
            self.M.insert(index, [0] * (n + 1))
        else:
            if n == 0:
                print("No vertex exists")
                return
            for i in range(n):
                self.M[i].pop(index)
            self.M.pop(index)

    def count_vertex_edge(self):
        sum_degree = 0
        vertex = len(self.M)
        for i in range(vertex):
            sum_degree += self.degree(i)
        edges = sum_degree//2
        return vertex, edges
        


