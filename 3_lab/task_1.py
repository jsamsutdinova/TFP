#!/usr/bin/env python3
""" Laboratory work 3. Task 3 """

class HashTable:
    """ 
        This class implements operations of a hash table.
        Use linear probling to avoid collision
    """

    def __init__(self, size=15):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def countHash (self, key, size):
        return key%size
    
    def linearProbling (self, old_hash, size):
        return (old_hash+1)%size
    
    def addItem (self, key, data):
        hash_key = self.countHash(key, len(self.slots))

        # Условие для случая, когда место в слоте пустое
        if self.slots[hash_key] == None:
            self.slots[hash_key] = key
            self.data[hash_key] = data
        else:
            # Если ключи совпали, обновляем значения данных,
            if self.slots[hash_key] == key:
                self.data[hash_key] = data
            else:
                # Иначе применяем линейное пробирование для избежания коллизии
                new_hash_key = self.linearProbling(hash_key, len(self.slots))
            
                while self.slots[new_hash_key] != None and self.slots[new_hash_key] != key:
                    new_hash_key = self.linearProbling(new_hash_key, len(self.slots))

                if self.slots[new_hash_key] == None:
                    # Добавляем в пустой слот значение ключа и данные
                    self.slots[new_hash_key] = key
                    self.data[new_hash_key] = data
                else:
                    # Если такой ключ уже есть, то обновляем данные
                    self.data[new_hash_key] = data

    def __additem__ (self, key, data):
        self.addItem(key, data)

if __name__ == '__main__':
    hash_table = HashTable()
    