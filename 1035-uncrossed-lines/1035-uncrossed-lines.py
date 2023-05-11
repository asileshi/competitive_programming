class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(i,j):
            if i>=len(nums1) or j>=len(nums2):
                return 0
            if (i,j) not in memo:
                if nums1[i] == nums2[j]:
                    memo[(i,j)] =  1+dp(i+1,j+1)
                else:
                    first = dp(i+1,j)
                    second = dp(i,j+1)
                    memo[(i,j)] =  max(first,second)
            return memo[(i,j)]
        return dp(0,0)