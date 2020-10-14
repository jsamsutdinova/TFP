#!/usr/bin/env python3
""" Laboratory work 3. Task 1 """

class HashTable:
    """
        This class implements operations of a hash table.
        Use tuple to avoid collision
    """

    def __init__(self, size=8):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @classmethod
    def count_hash (cls, key, size):
        """ Get hash key using remainder of a division """
        return key%size
    
    def add_item (self, key, data):
        """ Find empty slot and add new element to this slot"""
        hash_key = self.count_hash(key, len(self.slots))

        if self.slots[hash_key] is None:
            self.slots[hash_key] = key
            self.data[hash_key] = data
        else:
            if self.slots[hash_key] == key:
                self.data[hash_key] = data
            else:
                self.slots[hash_key] = (self.slots[hash_key], key,)
                self.data[hash_key] = (self.data[hash_key], data,)
    
    def get_item (self, key):
        """ Get item by key """
        initial_slot = self.count_hash(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = initial_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                print(key)
                print(self.slots[position])
                stop = True

        return data  

    def __setitem__(self, key, data):
        self.add_item(key, data)

    def __getitem__(self, key):
        return self.get_item(key)

if __name__ == '__main__':
    hash_table = HashTable()
    hash_table[20] = 'cat'
    hash_table[24] = 'dog'
    hash_table[32] = 'lion'
    print(hash_table.slots)
    print(hash_table.data)
    print(hash_table[32])
