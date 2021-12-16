class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smaller_list=[]
        for i in range(0,len(nums)):
            a=nums[i]
            count=0
            for j in nums:
                if a>j:
                    count+=1
            smaller_list.append(count)
        return smaller_listz 