# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs: return pairs

        def merge(pairs: List[Pair], s: int, m: int, e: int) -> None:
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

            # one of them will still have pairs
            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1

        def divideAndConquer(pairs: List[Pair], s: int, e: int) -> None:
            if s == e: return

            m = (s + e) // 2
            divideAndConquer(pairs, s, m)
            divideAndConquer(pairs, m+1, e)

            merge(pairs, s, m, e)

        divideAndConquer(pairs, 0, len(pairs)-1)
        return pairs