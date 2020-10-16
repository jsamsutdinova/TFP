#!/usr/bin/env python3
""" Laboratory work 3. Task 2 """

class HashTable:
    """
        This class implements operations of aa hash table.
        Use tuple to avoid collision
    """

    def __init__(self, size=8):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @classmethod
    def count_hash(cls, key, size):
        """ Get hash key using remainder of a division """
        return key%size

    def add_item(self, key, data):
        """ Find empty slot and add new element to this slot"""
        hash_key = self.count_hash(key, len(self.slots))

        if self.slots[hash_key] is None:
            self.slots[hash_key] = key
            self.data[hash_key] = data
        else:
            if self.slots[hash_key] == key:
                self.data[hash_key] = data
            elif isinstance(self.slots[hash_key], int):
                self.slots[hash_key] = [self.slots[hash_key], key]
                self.data[hash_key] = [self.data[hash_key], data]
            elif len(self.slots[hash_key]) > 1:
                self.slots[hash_key].append(key)
                self.data[hash_key].append(data)

    def get_item (self, key):
        """ Get item by key """
        search_slot = self.count_hash(key, len(self.slots))

        if self.slots[search_slot] == key:
            data = self.data[search_slot]
        elif isinstance(self.slots[search_slot], list):
            index_list = (self.slots[search_slot].index(key))
            data = (self.data[search_slot][index_list])
        else:
            data = None

        return data

    def delete_item(self, key):
        """ Delete item by key"""
        deleted_slot = self.count_hash(key, len(self.slots))

        if self.slots[deleted_slot] == key:
            self.slots[deleted_slot] = None
            self.data[deleted_slot] = None
        elif isinstance(self.slots[deleted_slot], list):
            index_list = (self.slots[deleted_slot].index(key))
            self.slots[deleted_slot].pop(index_list)
            self.data[deleted_slot].pop(index_list)

    def __setitem__(self, key, data):
        self.add_item(key, data)

    def __getitem__(self, key):
        return self.get_item(key)

    def __delitem__(self, key):
        return self.delete_item(key)

if __name__ == '__main__':
    hash_table = HashTable()
    hash_table[20] = "A hero of our Time"
    hash_table[45] = "Dead Souls"
    hash_table[32] = "Oblomov"
    hash_table[60] = "Fathers and Sons"
    hash_table[21] = "Crime and Punshment"
    hash_table[54] = "War and Peace"
    hash_table[33] = "Anna Karenina"
    hash_table[12] = "The Brothers Karamazov"
    print(hash_table.slots)
    print(hash_table.data)
    print(hash_table[21])
    del hash_table[60]
    print(hash_table.slots)
    print(hash_table.data)
