class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 0
        cur = -1
        l = i = 0
        while i<len(s):
            if ord(s[i])!=cur+1:
                ans = max(ans,i-l)
                l = i
            cur = ord(s[i])
            i+=1
        return max(ans,i-l)
    
        