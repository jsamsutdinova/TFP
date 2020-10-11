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

    @classmethod
    def count_hash (cls, key, size):
        """ Get hash key using remainder of a division """
        return key%size

    @classmethod
    def linear_probling (cls, old_hash, size):
        """ Solve collision problem """
        return (old_hash+1)%size

    def add_item (self, key, data):
        """ Find empty slot and add new element to this slot"""
        hash_key = self.count_hash(key, len(self.slots))

        # Условие для случая, когда место в слоте пустое
        if self.slots[hash_key] is None:
            self.slots[hash_key] = key
            self.data[hash_key] = data
        else:
            # Если ключи совпали, обновляем значения данных,
            if self.slots[hash_key] == key:
                self.data[hash_key] = data
            else:
                # Иначе применяем линейное пробирование для избежания коллизии
                new_hash_key = self.linear_probling(hash_key, len(self.slots))

                while self.slots[new_hash_key] is not None and self.slots[new_hash_key] != key:
                    new_hash_key = self.linear_probling(new_hash_key, len(self.slots))

                if self.slots[new_hash_key] is None:
                    # Добавляем в пустой слот значение ключа и данные
                    self.slots[new_hash_key] = key
                    self.data[new_hash_key] = data
                else:
                    # Если такой ключ уже есть, то обновляем данные
                    self.data[new_hash_key] = data


    def __setitem__(self, key, data):
        """ Special function for [] constraction """
        self.add_item(key, data)

if __name__ == '__main__':
    hash_table = HashTable()
