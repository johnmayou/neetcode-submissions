class Solution:

    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        q.append((0, 0))

        visited: set[tuple[int, int]] = set()

        depth = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == rows - 1 and col == cols - 1:
                    return depth

                for dr, dc in self.DIRECTIONS:
                    r = row + dr
                    c = col + dc
                    pos = (r, c)

                    if (
                        r < 0 or r >= rows
                        or c < 0 or c >= cols
                        or grid[r][c] == 1
                        or pos in visited
                    ):
                        continue

                    q.append(pos)
                    visited.add(pos)

            depth += 1

        return -1