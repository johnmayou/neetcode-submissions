class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0

        def backtrack(curr):
            nonlocal ways
            if curr == n:
                ways += 1
            elif curr < n:
                backtrack(curr + 1)
                backtrack(curr + 2)

        backtrack(1)
        backtrack(2)

        return ways