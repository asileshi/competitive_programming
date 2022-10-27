class Solution:
    def longestPrefix(self, s: str) -> str:
        table = [0]*len(s)
        i,j = 1,0
        while i<len(table):
            if s[i] == s[j]:
                table[i] = j+1
                j+=1
                i+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = table[j-1]
        return s[0:table[-1]]
        