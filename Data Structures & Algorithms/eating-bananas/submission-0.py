class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            m = (low + high) // 2
            if self.ableToEat(piles, h, m):
                res = m
                high = m - 1
            else:
                low = m + 1
        return res

    def ableToEat(self, piles: List[int], h: int, k: int) -> bool:
        for pile in piles:
            h -= math.ceil(pile / k)
            if h < 0:
                return False
        return True