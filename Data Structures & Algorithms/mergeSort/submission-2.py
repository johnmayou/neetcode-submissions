# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> None:
        if not pairs or s == e:
            return pairs

        m = (s + e) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m+1, e)

        self.merge(pairs, s, m, e)

        return pairs
    
    def merge(self, pairs: List[Pair], s: int, m: int, e: int) -> None:
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for pairs

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # one will still have values left
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1