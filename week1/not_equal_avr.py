class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        newlist=[]
        nums.sort()
        a=0
        b=len(nums)-1
        while len(newlist)!=len(nums):
            newlist.append(nums[a])
            a+=1
            if a<b:
                newlist.append(nums[b])
                b-=1
        return newlist