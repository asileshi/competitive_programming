class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r,stack = len(nums)-1,0,[]
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]]>num:
                l = min(l,stack.pop())
            stack.append(i)
        stack,i = [],len(nums)-1
        while i>=0:
            while stack and nums[stack[-1]]<nums[i]:
                r = max(r,stack.pop())
            stack.append(i)
            i-=1
        print(l,r)
        return r-l+1 if r-l>0 else 0