class Solution:
    def rob(self, nums: List[int]) -> int:
        chose = notchose = 0
        for i in range(len(nums)):
            temp = chose
            chose = notchose+nums[i]
            notchose = max(temp,notchose)
        return max(chose,notchose)
        