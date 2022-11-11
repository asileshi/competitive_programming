class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        per,idx = 0,len(nums)-1
        while idx-2>=0:
            if nums[idx]<nums[idx-1]+nums[idx-2]:
                per = max(per,nums[idx]+nums[idx-1]+nums[idx-2])
            idx-=1
        return per