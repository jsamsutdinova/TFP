#!/usr/bin/env python3
""" Code to insert a node in binary search tree """


class Node:
    """
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
        This function do preorder tree traversal
    """
    if root:
        print("{0} ".format(root.item), end="")
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
