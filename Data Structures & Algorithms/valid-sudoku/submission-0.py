class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n_rows = len(board)
        n_cols = len(board[0]) if board else 0

        rows = [set() for _ in range(n_rows)]
        cols = [set() for _ in range(n_cols)]

        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(n_rows):
            for c in range(n_cols):
                val = board[r][c]
                if val == ".":
                    continue

                box = boxes[r // 3][c // 3]

                if val in rows[r] or val in cols[c] or val in box:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                box.add(val)

        return True