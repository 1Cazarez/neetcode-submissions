class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols -1
        while start <= end:
            middle = (start + end) // 2
            value = matrix[middle // cols][middle % cols]
            if value == target:
                return True
            elif value < target:
                start = middle + 1
            else:
                end = middle - 1 
        return False
        