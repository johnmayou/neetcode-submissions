class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        pred, succ = self.tail.prev, self.tail
        new_node = Node(value)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node

    def appendleft(self, value: int) -> None:
        pred, succ = self.head, self.head.next
        new_node = Node(value)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        pred, succ = self.tail.prev.prev, self.tail
        popval = pred.next.val
        pred.next = succ
        succ.prev = pred
        return popval

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        pred, succ = self.head, self.head.next.next
        popval = pred.next.val
        pred.next = succ
        succ.prev = pred
        return popval
