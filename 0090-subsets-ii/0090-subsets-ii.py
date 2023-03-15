class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(2**len(nums)):
            temp = []
            bit = bin(i)[2:][::-1]
            for j in range(len(bit)):
                if bit[j] == '1':
                    temp.append(nums[j])
            ans.add(tuple(temp))
        return ans