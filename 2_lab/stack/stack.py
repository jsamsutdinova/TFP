 #!/usr/bin/env python3
""" The class for laboratory work 2 """
import numpy as np

class Stack:
    """ This class simulates work of stack """

    def __init__(self, stack):
        self.stack = stack

    def push(self):
        """ Add element to stack """
        new_item = int(input("New element: "))
        self.stack = np.append(self.stack, new_item)
        return self.stack, "Element added successfully!"

    def pop(self):
        """ Delete last element from stack"""
        if self.stack.size == 0:
            print ("Stack is empty")
        else:
            deleted_elem = self.stack[-1:]
            self.stack = self.stack[:-1]
            return deleted_elem

    def back(self):
        """Show last element """

        return self.stack[-1:]

    def size(self):
        """ Show size of steck """
        size_stack, = self.stack.shape
        return size_stack

    def clear(self):
        """ Clear stack """
        self.stack = np.array([])
        return "Stack is empty!"
