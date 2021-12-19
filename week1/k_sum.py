class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter=0
        a=0
        b=len(nums)-1
        nums.sort()
        while a<b:
            if nums[a]+nums[b]==k:
                counter+=1
                a+=1
                b-=1
            elif nums[a]+nums[b]<k:
                a+=1
            elif nums[a]+nums[b]>k:
                b-=1
        return counter