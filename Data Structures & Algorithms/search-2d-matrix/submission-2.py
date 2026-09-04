class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None

        left, right = 0, len(matrix) - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[m][0] > target:
                right = m - 1
            elif matrix[m][-1] < target:
                left = m + 1
            else:
                row = matrix[m]
                break

        if not row:
            return False

        left, right = 0, len(row) - 1
        while left <= right:
            m = (left + right) // 2
            if row[m] < target:
                left = m + 1
            elif row[m] > target:
                right = m - 1
            else:
                return True

        return False