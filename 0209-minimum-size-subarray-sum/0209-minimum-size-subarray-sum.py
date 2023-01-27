class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        temp = 0
        l = 0
        ans = inf
        i = 0
        while i<len(nums):
            if temp<target:
                temp+=nums[i]
                i+=1
            else:
                ans = min(ans,i-l)
                temp-=nums[l]
                l+=1  
        while target<=temp:
            ans = min(ans,i-l)
            temp-=nums[l]
            l+=1  
        return ans if ans!=inf else 0