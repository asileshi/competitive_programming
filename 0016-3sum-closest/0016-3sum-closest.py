import bisect
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = inf
        for i in range(len(nums)):
            l,r = 0,len(nums)-1
            while l<r and l!=i and r!=i:
                temp = nums[i]+nums[l]+nums[r]
                if abs(target-temp)<abs(target-ans):
                    ans = temp
                if temp>target:
                    r-=1
                else:
                    l+=1
        return ans
                
                