class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        table = [[0]*len(matrix[0]) for i in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='1':
                    l,d,t = 0,0,0
                    if i>=0:
                        t = table[i-1][j]
                    if j>=0:
                        l = table[i][j-1]
                    if i>=0 and j>=0:
                        d = table[i-1][j-1]
                    table[i][j] = 1+min(l,d,t)
                    ans = max(ans,(table[i][j])**2)
        return ans