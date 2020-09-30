 #!/usr/bin/env python3
""" The class for laboratory work 2 """
import numpy as np

class Deque:
    """
        This class simulates work of deque
    """
    def __init__(self, array):
        self.deque = array

    def push_front (self):
        """
            Add new item to beginning of deque
        """
        new_item = int(input("New item to beggining: "))
        self.deque = np.insert(self.deque, 0, new_item)
        return self.deque

    def push_back (self):
        """
            Add new item to the end of deque
        """
        new_item = int(input("New item to the end: "))
        self.deque = np.append(self.deque, new_item)
        return self.deque

    def pop_front (self):
        """
            Delete first item from deque
        """
        if self.deque.size == 0:
            print ("Deque is empty")
        else:
            deleted_item = self.deque[:1]
            self.deque = np.delete(self.deque, 0)
            return deleted_item

    def pop_back (self):
        """
            Delete last item from deque
        """
        if self.deque.size == 0:
            print ("Deque is empty")
        else:
            deleted_item = self.deque[-1:]
            self.deque = self.deque[:-1]
            return deleted_item

    def front (self):
        """
            Show first item of deque
        """
        return self.deque[:1]

    def back (self):
        """
            Show last item of deque
        """
        return self.deque[-1:]

    def size (self):
        """
            Show size of deque
        """
        size_deque, = self.deque.shape
        return size_deque

    def clear (self):
        """
            Clear deque
        """
        self.deque = np.array([])
        return "Deque is empty!"
        