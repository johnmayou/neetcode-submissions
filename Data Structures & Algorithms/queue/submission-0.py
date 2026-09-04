class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        pred, succ = self.tail.prev, self.tail
        node = Node(value, pred, succ)
        pred.next = node
        succ.prev = node
        self.size += 1

    def appendleft(self, value: int) -> None:
        pred, succ = self.head, self.head.next
        node = Node(value, pred, succ)
        pred.next = node
        succ.prev = node
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        pred, succ = self.tail.prev.prev, self.tail
        popval = pred.next.val
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return popval

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        pred, succ = self.head, self.head.next.next
        popval = pred.next.val
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return popval
