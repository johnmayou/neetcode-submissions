# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._quickSort(pairs, 0, len(pairs) - 1)

    def _quickSort(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        swap = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[swap], arr[i] = arr[i], arr[swap]
                swap += 1

        arr[swap], arr[e] = arr[e], arr[swap]

        self._quickSort(arr, s, swap - 1)
        self._quickSort(arr, swap + 1, e)

        return arr
