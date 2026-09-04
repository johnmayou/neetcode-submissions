# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._sort(pairs, 0, len(pairs) - 1)

    def _sort(self, arr: list[Pair], s: int, e: int) -> list[Pair]:
        if e - s <= 0:
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        # Move pivot.
        arr[left], arr[e] = arr[e], arr[left]

        self._sort(arr, s, left - 1)
        self._sort(arr, left + 1, e)

        return arr