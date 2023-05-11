class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            c = 0
            for num in nums:
                if num&(1<<i):
                    c+=1
            if c%3:
                ans|=(1<<i)
        return ans if ans<(1<<31) else ans-(1<<32)