# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSort(pairs, 0, len(pairs) - 1)

    def _mergeSort(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s <= 0:
            return arr

        m = (s + e) // 2
        self._mergeSort(arr, s, m)
        self._mergeSort(arr, m + 1, e)
        self._merge(arr, s, m, e)

        return arr

    def _merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        l_arr = arr[s: m + 1]
        r_arr = arr[m + 1: e + 1]

        i = 0 # index for l_arr
        j = 0 # index for r_arr
        k = s # index for arr

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i].key <= r_arr[j].key:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        # one will have remaining values
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1
        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1