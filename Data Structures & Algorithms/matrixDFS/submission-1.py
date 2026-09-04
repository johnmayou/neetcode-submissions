class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        paths = 0

        def dfs(r, c):
            nonlocal paths
            if c < 0 or r < 0 or c >= cols or r >= rows or grid[r][c] == 1:
                return
            if r == rows - 1 and c == cols - 1:
                paths += 1
                return

            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            grid[r][c] = 0

        dfs(0, 0)
        return paths