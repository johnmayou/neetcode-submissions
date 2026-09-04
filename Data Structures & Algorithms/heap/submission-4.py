class MinHeap:
    def __init__(self):
        self.arr = [0]

    def push(self, val: int) -> None:
        self.arr.append(val)
        self._up(len(self.arr) - 1)

    def pop(self) -> int:
        if self.empty():
            return -1
        if len(self.arr) == 2:
            return self.arr.pop()

        popval = self.arr[1]
        self.arr[1] = self.arr.pop()
        self._down(1)

        return popval

    def top(self) -> int:
        return -1 if self.empty() else self.arr[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            self.arr = [0]
            return

        self.arr = nums
        self.arr.append(self.arr[0])
        self.arr[0] = 0

        for i in range(len(self.arr) // 2, -1, -1):
            self._down(i)

    def empty(self) -> None:
        return len(self.arr) == 1

    def _up(self, i: int) -> None:
        while i // 2 > 0 and self.arr[i // 2] > self.arr[i]:
            self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
            i //= 2

    def _down(self, i: int) -> None:
        while i * 2 < len(self.arr):
            if (
                i * 2 + 1 < len(self.arr)
                and self.arr[i * 2 + 1] < self.arr[i * 2]
                and self.arr[i * 2 + 1] < self.arr[i]
            ):
                # Swap with right.
                self.arr[i], self.arr[i * 2 + 1] = self.arr[i * 2 + 1], self.arr[i]
                i = i * 2 + 1
            elif self.arr[i * 2] < self.arr[i]:
                # Swap with left.
                self.arr[i], self.arr[i * 2] = self.arr[i * 2], self.arr[i]
                i *= 2
            else:
                break