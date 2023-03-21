class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        temp = 0
        ans = 0
        for num in nums:
            if num!=0:
                ans+=((temp+1)*temp//2)
                temp = 0
            else:
                temp+=1
        return ans+(temp+1)*temp//2