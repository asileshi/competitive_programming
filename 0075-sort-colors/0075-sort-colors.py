class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r,w,b = 0,0,0
        for i in nums:
            if i == 0:
                r+=1
            elif i == 1:
                w+=1
            else:
                b+=1
        idx = 0
        for i in range(r):
            nums[idx] = 0
            idx+=1
        for i in range(w):
            nums[idx] = 1
            idx+=1
        for i in range(b):
            nums[idx] = 2
            idx+=1
        