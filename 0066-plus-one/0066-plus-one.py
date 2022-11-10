class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        i=0
        while i<len(digits):
            ans*=10
            ans+=digits[i]
            i+=1
        return list(str(ans+1))
        