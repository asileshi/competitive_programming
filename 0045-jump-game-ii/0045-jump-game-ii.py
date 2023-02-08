class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        left = right = 0
        while right<len(nums)-1:
            end = 0
            for i in range(left,right+1):
                end = max(end,i+nums[i])
            left = right
            right = end
            ans+=1
        return ans
            
            