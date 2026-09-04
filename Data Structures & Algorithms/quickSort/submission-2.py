# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._quickSort(pairs, 0, len(pairs) - 1)
        
    def _quickSort(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s <= 0:
            return arr

        pivot = arr[e]
        left = s
        for right in range(s, e):
            if arr[right].key < pivot.key:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1

        arr[left], arr[e] = arr[e], arr[left]

        self._quickSort(arr, s, left - 1)
        self._quickSort(arr, left + 1, e)

        return arr