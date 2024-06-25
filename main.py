"""
add 
remove
randomly pick a number

data = integers, unique
O(1)

hashmaps in O(1)
dictionary in python

"""
from collections import defaultdict
from random import randint


class DataStore:
    def __init__(self) -> None:
        self.val_index_map = defaultdict(int)
        self.data = list()
        self.size = 0

    def add(self, val):
        self.data.append(val)
        self.val_index_map[val] = self.size
        self.size += 1

    def remove(self, key):
        if key not in self.val_index_map:
            return -1
        key_index = self.val_index_map[key]
        self.data[key_index] = self.data[-1]
        self.data.pop()
        del (self.val_index_map, key)
        self.size -= 1

    def get_random(self):
        random_index = randint(0, self.size - 1)
        return self.data[random_index]


def main():
    store = DataStore()
    operations = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 2],
        [3]
    ]

    for operation in operations:
        if operation[0] == 1:
            store.add(operation[1])
        elif operation[0] == 2:
            store.remove(operation[1])
        else:
            print(store.get_random())


if __name__ == '__main__':
    main()
