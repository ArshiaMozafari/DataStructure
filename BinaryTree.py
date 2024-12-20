#Binary tree is a data structure retrieved from tree concepts that each parent can have at most 2 children.


class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, data):
        new_node = BinaryNode(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp.Lchild:
                temp = temp.Lchild
            temp.Lchild = new_node

    def insert_right(self, data):
        new_node = BinaryNode(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp.Rchild:
                temp = temp.Rchild
            temp.Rchild = new_node

    def preorder(self):
        self._preorder(self.root)
    
    def _preorder(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder(node.Lchild)
            self._preorder(node.Rchild)
    
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, node):
        if node:
            self._inorder(node.Lchild)
            print(node.data, end=" ")
            self._inorder(node.Rchild)
    
    def postorder(self):
        self._postorder(self.root)
    
    def _postorder(self, node):
        if node:
            self._postorder(node.Lchild)
            self._postorder(node.Rchild)
            print(node.data, end=" ")

    def level_order(self):
        if self.root is None:
            return
        list = []
        list.append(self.root)
        while len(list) > 0:
            temp = list.pop(0)
            print(temp.data, end=" ")
            if temp.Lchild:
                list.append(temp.Lchild)
            if temp.Rchild:
                list.append(temp.Rchild)


    def insert_after_l(self, x, data):
        self._insert_after_l(self.root, x, data)

    def _insert_after_l(self, node, x, data):
        if node:
            if node.data == x:
                temp = node.Lchild
                node.Lchild = BinaryNode(data)
                node.Lchild.Lchild = temp
            self._insert_after_l(node.Lchild, x, data)
            self._insert_after_l(node.Rchild, x, data)

    def insert_after_r(self, x, data):
        self._insert_after_r(self.root, x, data)

    def _insert_after_r(self, node, x, data):
        if node:
            if node.data == x:
                temp = node.Rchild
                node.Rchild = BinaryNode(data)
                node.Rchild.Rchild = temp
            self._insert_after_r(node.Lchild, x, data)
            self._insert_after_r(node.Rchild, x, data)

    def delete_left(self):
        if not self.root:
            print("Tree is empty")
            return
        temp = self.root
        while temp.Lchild and (temp.Lchild.Lchild or temp.Lchild.Rchild):
            temp = temp.Lchild
        if temp.Lchild:
            temp.Lchild = None

    def delete_right(self):
        if not self.root:
            print("Tree is empty")
            return
        temp = self.root
        while temp.Rchild and (temp.Rchild.Lchild or temp.Rchild.Rchild):
            temp = temp.Rchild
        if temp.Rchild:
            temp.Rchild = None

    def delete_x(self, x):
        if not self.root:
            print("Tree is empty")
            return
        # Special case when the root itself is the node to be deleted
        if self.root.data == x:
            self.root = None
            return
        self._delete(self.root, x)

    def _delete(self, node, x):
        if node:
            if node.Lchild and node.Lchild.data == x:
                node.Lchild = None
                return
            if node.Rchild and node.Rchild.data == x:
                node.Rchild = None
                return
            self._delete(node.Lchild, x)
            self._delete(node.Rchild, x)

    def delete_left_x(self, x):
        if not self.root:
            print("Tree is empty")
            return
        self._delete_left_x(self.root, x)

    def _delete_left_x(self, node, x):
        if node:
            if node.Lchild and node.Lchild.data == x:
                if node.Lchild.Lchild:
                    node.Lchild.Lchild = None
                return
            self._delete_left_x(node.Lchild, x)
            self._delete_left_x(node.Rchild, x)

    def delete_right_x(self, x):
        if not self.root:
            print("Tree is empty")
            return
        self._delete_right_x(self.root, x)

    def _delete_right_x(self, node, x):
        if node:
            if node.Rchild and node.Rchild.data == x:
                if node.Rchild.Rchild:
                    node.Rchild.Rchild = None
                return
            self._delete_right_x(node.Lchild, x)
            self._delete_right_x(node.Rchild, x)

    
