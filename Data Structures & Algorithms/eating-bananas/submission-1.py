class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = high
        while low <= high:
            m = (low + high) // 2
            if self.canEatAll(piles, h, m):
                k = m
                high = m - 1
            else:
                low = m + 1
        return k

    def canEatAll(self, piles: List[int], h: int, k: int):
        for pile in piles:
            h -= math.ceil(pile / k)
            if h < 0:
                return False
        return True