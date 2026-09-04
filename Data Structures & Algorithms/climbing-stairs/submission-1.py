class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0

        def recurse(curr):
            nonlocal ways
            if curr == n:
                ways += 1
            elif curr < n:
                recurse(curr + 1)
                recurse(curr + 2)

        recurse(0)

        return ways