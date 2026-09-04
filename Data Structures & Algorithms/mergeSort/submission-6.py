# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSort(pairs, 0, len(pairs) - 1)

    def _mergeSort(self, arr: list[Pair], s: int, e: int) -> list[Pair]:
        if e - s <= 0:
            return arr

        m = (s + e) // 2
        self._mergeSort(arr, s, m)
        self._mergeSort(arr, m + 1, e)

        self._merge(arr, s, m, e)

        return arr

    def _merge(self, arr: list[Pair], s: int, m: int, e: int) -> None:
        left, right = arr[s:m + 1], arr[m + 1:e + 1]
        l, r = 0, 0

        # index for arr insertion
        k = s

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1