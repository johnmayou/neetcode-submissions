# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._quickSort(pairs, 0, len(pairs) - 1)
    
    def _quickSort(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e].key
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        # swap pivot
        pairs[left], pairs[e] = pairs[e], pairs[left]

        # sort left side
        self._quickSort(pairs, s, left - 1)

        # sort right side
        self._quickSort(pairs, left + 1, e)

        return pairs