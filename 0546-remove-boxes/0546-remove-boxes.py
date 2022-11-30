class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l,r,c):
            if l>r:
                return 0
            while l+1<r and boxes[l] == boxes[l+1]:
                l+=1
                c+=1
            c+=1
            temp = c**2+dp(l+1,r,0)
            for i in range(l+1,r+1):
                if boxes[l] == boxes[i]:
                    temp = max(temp,dp(i,r,c)+dp(l+1,i-1,0))
            return temp
        return dp(0,len(boxes)-1,0)