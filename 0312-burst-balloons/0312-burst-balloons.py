class Solution:
    def maxCoins(self, nums: List[int]) -> int:
            nums = [1] + nums + [1] 
            table = [[0] * len(nums) for _ in range(len(nums))]
            for d in range(2, len(nums)):
                for i in range(len(nums)-d):
                    j = i + d
                    for k in range(i+1, j):
                        table[i][j] = max(table[i][j], nums[i] * nums[k] * nums[j] + table[i][k] + table[k][j])
            return table[0][len(nums)-1]