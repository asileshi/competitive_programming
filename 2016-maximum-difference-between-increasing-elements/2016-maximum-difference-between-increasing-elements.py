class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn = inf
        ans = -1
        for num in nums:
            if num<=minn:
                minn = num
            else:
                ans = max(num-minn,ans)
        return ans
        
        