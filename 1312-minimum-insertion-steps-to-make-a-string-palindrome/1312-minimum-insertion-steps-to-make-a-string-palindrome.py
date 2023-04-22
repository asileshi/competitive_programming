class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def dp(i,j):
            if i>=j:
                return 0
            if (i,j) not in memo:
                if s[i]!=s[j]:
                    memo[(i,j)] = 1+(min(dp(i+1,j),dp(i,j-1)))
                else:
                    memo[(i,j)] = dp(i+1,j-1)
            return memo[(i,j)]
        return dp(0,len(s)-1)
    