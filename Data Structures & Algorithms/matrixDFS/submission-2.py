class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited: set[int] = set()
        def dfs(r: int, c: int) -> int:
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or grid[r][c] == 1
                or (r, c) in visited
            ):
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1
            
            visited.add((r, c))

            paths = 0
            paths += dfs(r - 1, c)
            paths += dfs(r + 1, c)
            paths += dfs(r, c - 1)
            paths += dfs(r, c + 1)

            visited.remove((r, c))

            return paths

        return dfs(0, 0)