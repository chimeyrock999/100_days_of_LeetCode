class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row = 0
        last_row = len(matrix)-1
        while first_row <= last_row :
            mid_row = (first_row+last_row)//2
            if matrix[mid_row][-1] < target:
                first_row = mid_row + 1
            elif matrix[mid_row][0] > target:
                last_row = mid_row - 1
            else:
                break
        
        if first_row > last_row:
            return False
        
        curr_row = (first_row+last_row)//2
        L = 0
        R = len(matrix[curr_row])-1
        while L<=R:
            mid = (L+R)//2
            if matrix[curr_row][mid] < target:
                L = mid +1
            elif matrix[curr_row][mid] > target:
                R = mid - 1
            else:
                return True
        return False

