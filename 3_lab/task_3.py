#!/usr/bin/env python3
""" Laboratory work 3. Task 3 """

class HashTable:
    """
        This class implements operations of a hash table.
        Use linear probling to avoid collision
    """

    def __init__(self, size=8):
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

    def get_item (self, key):
        """ Get item by key """
        initial_slot = self.count_hash(key, len(self.slots))

        # Устанавливаем начальные параметры для поиска
        data = None
        stop = False
        found = False
        position = initial_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.linear_probling(position, len(self.slots))
                if position == initial_slot:
                    stop = True

        return data

    def delete_item (self, key):
        """ Delete item by key """
        initial_slot = self.count_hash(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = initial_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None
            else:
                position = self.linear_probling(position, len(self.slots))
                if position == initial_slot:
                    stop = True
                    self.slots[position] = None
                    self.data[position] = None

        return data

    def __getitem__(self, key):
        return self.get_item(key)

    def __setitem__(self, key, data):
        """ Special function for [] constraction """
        self.add_item(key, data)

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
    print(hash_table[32])
    del hash_table[54]
    print(hash_table.slots)
    print(hash_table.data)
