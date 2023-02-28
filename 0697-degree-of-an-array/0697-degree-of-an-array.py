class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        idx = {nums[i]:[0,-1,-1] for i in range(len(nums))}
        for i,num in enumerate(nums):
            idx[num][0]+=1
            if idx[num][1] == -1:
                idx[num][1] = i
            idx[num][2] = i
        degree = [[-idx[num][0],idx[num][2]-idx[num][1]+1] for num in idx]
        degree.sort()
        return degree[0][1]