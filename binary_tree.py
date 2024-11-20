# Binary Tree
from collections import deque

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        if self.left_child == None:
            # create a new node and set it as leftchild
            self.left_child = BinaryTree(value)
        else:
            # create a new node and set it to current node's left child
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child 
            self.left_child = new_node
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()
    
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        
        if self.right_child:
            self.right_child.post_order()
        
        print(self.value)
    
    def bfs(self):
        queue = deque()
        queue.append(self)

        while len(self.queue) != 0:
            current_node = self.queue.popleft()
            print(current_node.value)

            if current_node.left_child:
                queue.append(current_node.left_child)
            
            if current_node.right_child:
                queue.append(current_node.right_child)






    

tree = BinaryTree('a')
print(tree.value) # a
print(tree.left_child) # None
print(tree.right_child) # None

"""
DFS:
Start at the root-> explore deep down the leaf->backtrack

Types of DFS
1. Pre-order (P->L->R)
- Print the value of the node.
- Go to the left child and print it, if it exists.
- Go to the right child and print it, if it exists.

2. In-order (L->P->R)
- Go to the left child and print it, if it exists.
- Print the node’s value
- Go to the right child and print it, if it exists.

3. Post-order (L->R->P)
- Go to the left child and print it, if it exists.
- Go to the right child and print it, if it exists.
- Print the node’s value

BFS:
Start at the root -> explore neighbors -> move to the next level neighbors...

Algorithm, using queue data structure:
- First add the root node into the queue.
- Iterate while the queue is not empty.
- Get the first node in the queue, and then print its value.
- Add both left and right children into the queue (if the current nodehas children).
- Print the value of each node, level by level, with the queue helper
"""

    