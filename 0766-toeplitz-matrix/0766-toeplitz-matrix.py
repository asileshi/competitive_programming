class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if 0<=i+1<len(matrix) and 0<=j+1<len(matrix[0]):
                    if matrix[i][j]!=matrix[i+1][j+1]:
                        return False
                    
                    
        return True