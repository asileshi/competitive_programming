class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for num in nums:
            temp^=num
        one = 0
        for i in range(32):
            if temp&(1<<i):
                break
        for num in nums:
            if num&(1<<i):
                one^=num
        two = temp^one
        return [one if one<(1<<31) else one-(1<<32),two if two<(1<<31) else two-(1<<32)]