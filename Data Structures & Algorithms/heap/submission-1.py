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

        # replace with last value
        self.heap[1] = self.heap.pop()

        # perculate down
        i = 1
        while i * 2 < len(self.heap):
            if (
                i * 2 + 1 < len(self.heap) and
                self.heap[i * 2 + 1] < self.heap[i * 2] and
                self.heap[i] > self.heap[i * 2 + 1]
            ):
                # swap right node
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[i * 2]:
                # swap left node
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = 2 * i
            else:
                break

        return result

    def top(self) -> int:
        return -1 if len(self.heap) == 1 else self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            self.heap = [0]
            return

        self.heap = nums
        self.heap.append(nums[0])

        # perculate down all nodes with children
        curr = (len(self.heap) - 1) // 2
        while curr > 0:
            i = curr

            if (
                i * 2 + 1 < len(self.heap) and
                self.heap[i * 2 + 1] < self.heap[i * 2] and
                self.heap[i] > self.heap[i * 2 + 1]
            ):
                # swap right node
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[i * 2]:
                # swap left node
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = 2 * i

            curr -= 1
        