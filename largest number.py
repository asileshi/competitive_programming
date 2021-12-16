class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        else:
            for i in range(0,len(nums)):
                for j in range (0,len(nums)-1):
                    if int(str(nums[j])+str(nums[j+1])) < int(str(nums[j+1])+str(nums[j])):
                        nums[j],nums[j+1]=str(nums[j+1]),str(nums[j])
                    else:
                        nums[j],nums[j+1]=str(nums[j]),str(nums[j+1])
                
        if int(nums[0])==0:
            return str(0)
        else:
            return "".join(nums)