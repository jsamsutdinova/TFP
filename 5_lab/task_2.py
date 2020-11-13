#!/usr/bin/env python3
""" Code to insert a node in balanced binary tree (AVL) """


class Node(object):
    """
        Represents an individual node in a BST
    """
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item
        self.height = 1


class AVL_Tree(object):
    """
        Class implements the insert operation to the tree
    """
    def insert(self, root, key):

        # Create normal BST
        if root is None:
            return Node(key)
        else:
            if root.item == key:
                return root
            elif root.item < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)

        # Update the height of the parent node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # If the node is unbalanced, then try 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.item:
            return self.rightRotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.item:
            return self.leftRotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.item:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.item:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, item):
        """
            Shifts to the left subtree
        """
        y = item.right
        T2 = y.left

        # Perform rotation
        y.left = item
        item.right = T2

        # Update heights
        item.height = 1 + max(self.getHeight(item.left),
                              self.getHeight(item.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, item):
        """
            Shifts to the right subtree
        """
        y = item.left
        T3 = item.right

        # Perform rotation
        y.right = item
        item.left = T3

        # Update heights
        item.height = 1 + max(self.getHeight(item.left),
                              self.getHeight(item.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        """
            Check availability of root.
            Return height 0 or 1
        """
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        """
            Return balance factor of node
        """
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preorder(self, root):
        if not root:
            return

        print("{0} ".format(root.item), end="")
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    tree = AVL_Tree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    tree.preorder(root)
    print()
