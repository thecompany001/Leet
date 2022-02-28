class Solution(object):
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        #determine which rows/cols need to be zero
        for r in range(ROWS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][r] == 0 or matrix[r][0] == 0:
                    matrix[r][x] = 0
                
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0