class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)

        # percolate up
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()

        result = self.heap[1]
        self.heap[1] = self.heap.pop() # replace with last node
        # percolate down
        i = 1
        while i * 2 < len(self.heap):
            if (
                i * 2 + 1 < len(self.heap) and # right node exists
                self.heap[i * 2 + 1] < self.heap[i * 2] and # right is less than left
                self.heap[i] > self.heap[i * 2 + 1]
            ):
                # replace with right node
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                # replace with left node
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i *= 2
            else:
                break

        return result

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            self.heap = [0]
            return

        self.heap = nums
        self.heap.append(self.heap[0]) # heap uses 1 based indexing

        curr = (len(self.heap) - 1) // 2 # first node with children
        while curr > 0:
            # percolate down
            i = curr
            while i * 2 < len(self.heap):
                if (
                    i * 2 + 1 < len(self.heap) and # right node exists
                    self.heap[i * 2 + 1] < self.heap[i * 2] and # right is less than left
                    self.heap[i] > self.heap[i * 2 + 1]
                ):
                    # replace with right node
                    self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                elif self.heap[i] > self.heap[i * 2]:
                    # replace with left node
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i *= 2
                else:
                    break

            curr -= 1