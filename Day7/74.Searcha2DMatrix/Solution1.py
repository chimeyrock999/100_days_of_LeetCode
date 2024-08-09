class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        n_col = len(matrix[0])
        n_row = len(matrix)
        R = n_col*n_row - 1

        while L<=R:
            mid = (L+R)//2
            curr_row = mid//n_col
            curr_col = mid%n_col
            if matrix[curr_row][curr_col] < target:
                L = mid + 1
            elif matrix[curr_row][curr_col] > target:
                R = mid -1
            else:
                return True
        return False
