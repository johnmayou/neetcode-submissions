class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()

        def dfs(r: int, c: int):
            if (
                r < 0 or r == rows or # row out of range
                c < 0 or c == cols or # col out of range
                (r, c) in visited or # already visited
                grid[r][c] == 1 # rock (blocked path)
            ):
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            visited.add((r, c))
            count = (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
            visited.remove((r, c)) # backtrack

            return count

        return dfs(0, 0)