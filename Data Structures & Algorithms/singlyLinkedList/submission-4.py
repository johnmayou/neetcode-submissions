class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.tail = Node(-1) # dummy
        self.head = Node(-1, self.tail) # dummy
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next
        new_node = Node(val)
        new_node.next = succ
        pred.next = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.tail

        pred = self.head
        for _ in range(self.length):
            pred = pred.next
        pred.next = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length or index < 0:
            return False

        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next
        self.length -= 1

        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr is not self.tail:
            vals.append(curr.val)
            curr = curr.next
        return vals
