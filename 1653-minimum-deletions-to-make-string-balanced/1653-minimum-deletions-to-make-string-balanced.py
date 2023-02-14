class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0
        for l in s:
            if l == "b":
                bCount += 1
                        
        ans = bCount
        cur = bCount
        for l in s:
            if l == "b":
                cur -= 1
            else:
                cur += 1
            ans = max(ans, cur)
        
        return len(s) - ans
        