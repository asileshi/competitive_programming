class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i, nums[j] - nums[i]) in table:
                    table[j, nums[j] - nums[i]] = table[(i, nums[j] - nums[i])]+1
                else:
                    table[(i, nums[j] - nums[i])] = 1
                    table[j, nums[j] - nums[i]] = table[(i, nums[j] - nums[i])]+1
                                    
        ans = 0
        for i in table:
            ans = max(ans,table[i])
        return ans