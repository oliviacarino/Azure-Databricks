# Binary Tree Implementation
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

    # Postorder traversal (DFS)
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    # BFS Implemnetaion
    def bfs(self, root):
        if root is None:
            return
        queue = deque()
        queue.append(root)

        while queue:
            cur_node = queue.popleft()
            print(cur_node.data)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
#root.PrintTree()
#print(root.PostorderTraversal(root)) # Correct Output: [10, 19, 14, 31, 42, 35, 27]
root.bfs(root) # 27 14 35 10 19 31 42
