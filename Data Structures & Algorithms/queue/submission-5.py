class Node:
    def __init__(self, val: int) -> None:
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
        
    # Add to tail.
    def append(self, value: int) -> None:
        prev, succ = self.tail.prev, self.tail
        node = Node(value)
        node.prev = prev
        node.next = succ
        prev.next = node
        succ.prev = node
        
    # Add to head.
    def appendleft(self, value: int) -> None:
        prev, succ = self.head, self.head.next
        node = Node(value)
        node.prev = prev
        node.next = succ
        prev.next = node
        succ.prev = node

    # Remove from tail.
    def pop(self) -> int:
        if self.isEmpty():
            return -1

        prev, succ = self.tail.prev.prev, self.tail
        popval = prev.next.val
        prev.next = succ
        succ.prev = prev
        return popval
        
    # Remove from head.
    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        prev, succ = self.head, self.head.next.next
        popval = prev.next.val
        prev.next = succ
        succ.prev = prev
        return popval
