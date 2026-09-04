class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if self.head == self.tail:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        if prev.next is None:
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        vals: list[int] = []
        curr = self.head.next
        for _ in range(self.size):
            vals.append(curr.val)
            curr = curr.next
        return vals