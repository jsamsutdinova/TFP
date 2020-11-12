#!/usr/bin/env python3
""" Laboratory work 5. Task 1 """


class Node:
    """
        This class imlements insert operation in binary search tree (BST).
        Represents an individual node in a BST
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.item = key


def insert(root, key):
    """
        This function to insert a new node
    """
    if root is None:
        return Node(key)
    else:
        if root.item == key:
            return root
        elif root.item < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
        return root


def preorder(root):
    """
        This function to to do preorder tree traversal
    """
    if root:
        print(root.item)
        preorder(root.left)
        preorder(root.right)


bst = Node(50)
bst = insert(bst, 30)
bst = insert(bst, 20)
bst = insert(bst, 80)
bst = insert(bst, 60)
bst = insert(bst, 40)
bst = insert(bst, 70)

preorder(bst)

print('left')
preorder(bst.left)

print('right')
preorder(bst.right)
