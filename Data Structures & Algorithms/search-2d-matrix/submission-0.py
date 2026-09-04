class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                row = matrix[i]
            else:
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

        
