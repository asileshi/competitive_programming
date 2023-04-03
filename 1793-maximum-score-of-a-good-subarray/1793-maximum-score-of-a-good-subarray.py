class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left,right = [0]*len(nums),[len(nums)-1]*len(nums)
        stack = []
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]]>num:
                right[stack.pop()] = i-1
            stack.append(i)
        i = len(nums)-1
        stack = []
        while i>=0:
            while stack and nums[stack[-1]]>nums[i]:
                left[stack.pop()] = i+1
            stack.append(i)
            i-=1
        ans = -inf
        for i in range(len(nums)):
            if left[i]<=k<=right[i]:
                ans = max(ans,nums[i]*(right[i]-left[i]+1))
        return ans
        