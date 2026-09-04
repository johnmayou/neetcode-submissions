class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.map = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        if self.map[index]:
            prev, curr = None, self.map[index]
            while curr:
                if curr.key == key:
                    # update value
                    curr.val = value
                    return
                prev = curr
                curr = curr.next

            # existing not found, add new node
            prev.next = Node(key, value)
        else:
            # insert new
            self.map[index] = Node(key, value)

        self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)

        curr = self.map[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        prev, curr = None, self.map[index]
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.map[index] = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        newMap = [None] * self.capacity

        for node in self.map:
            while node:
                index = self.hash(node.key)
                if newMap[index]:
                    curr = newMap[index]
                    while curr.next:
                        curr = curr.next
                    curr.next = Node(node.key, node.val)
                else:
                    newMap[index] = Node(node.key, node.val)
                node = node.next

        self.map = newMap