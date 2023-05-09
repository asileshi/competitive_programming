class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        mx = int('1'*len(nums),2)
        for i in range(mx+1):
            tempans = []
            temp = bin(i)[2:][::-1]
            for j in range(len(temp)):
                if temp[j] == '1':
                    tempans.append(nums[j])
            ans.append(tempans)
        return ans