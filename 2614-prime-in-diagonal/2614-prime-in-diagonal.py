class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if (n%i) == 0:
                  return False
            return True
        i,j = 0,0
        i,j = 0,0
        ans = 0
        while i<len(nums) and j<len(nums[i]):
            if is_prime(nums[i][j]):
                ans = max(ans,nums[i][j])
            i+=1
            j+=1
        i,j  = 0,len(nums[0])-1
        while i<len(nums) and j>=0:
            if is_prime(nums[i][j]):
                ans = max(ans,nums[i][j])
            i+=1
            j-=1
        return ans
            
            