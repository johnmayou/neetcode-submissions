class Pair:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.len = 0

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while self.arr[index] is not None:
            pair = self.arr[index]
            if pair.key == key:
                pair.val = value
                return
            index += 1
            index %= self.capacity
        
        self.arr[index] = Pair(key, value)
        self.len += 1

        if self.len / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)

        while pair := self.arr[index]:
            if pair.key == key:
                return pair.val
            index += 1
            index %= self.capacity

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while pair := self.arr[index]:
            if pair.key == key:
                self.arr[index] = None
                self.len -= 1
                return True
            index += 1
            index %= self.capacity

        return False

    def getSize(self) -> int:
        return self.len

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2

        old = self.arr
        self.arr = [None] * self.capacity
        self.len = 0

        for pair in old:
            if pair:
                self.insert(pair.key, pair.val)

    def hash(self, key: int) -> None:
        return key % self.capacity