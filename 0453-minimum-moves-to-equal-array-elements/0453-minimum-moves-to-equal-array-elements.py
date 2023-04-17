class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        ans = 0
        for num in nums:
            ans+=(num-mn)
        return ans