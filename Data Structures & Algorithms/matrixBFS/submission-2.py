class Solution:

    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        depth = 0
        queue = deque([(0, 0)])
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == rows - 1 and col == cols - 1:
                    return depth

                grid[row][col] = 1 # don't revisit

                for dr, dc in Solution.DIRECTIONS:
                    r = dr + row
                    c = dc + col
                    if (
                        r < 0 or r >= rows or
                        c < 0 or c >= cols or
                        grid[r][c] == 1
                    ):
                        continue
                    queue.append((r, c))
            depth += 1
        
        return -1