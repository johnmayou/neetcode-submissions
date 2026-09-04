class Solution:

    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        q = deque()
        q.append((0, 0))
        visited: set[tuple[int, int]] = set()
        visited.add((0, 0))

        length = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == rows - 1 and col == cols - 1:
                    return length

                for dr, dc in self.DIRECTIONS:
                    r = row + dr
                    c = col + dc
                    if (0 <= r < rows and 0 <= c < cols and
                        (r, c) not in visited and grid[r][c] == 0):
                            visited.add((r, c))
                            q.append((r, c))
            length += 1

        return -1






