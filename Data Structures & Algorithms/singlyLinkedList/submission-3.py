class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:  
    def __init__(self):
        self.head = Node(-1) # dummy
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # find node before index
        curr = self.head # dummy node (index -1)
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
