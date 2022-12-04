class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        ans = inf
        val = inf
        for i in range(len(prefix)-1):
            if abs(prefix[i]//(i+1)-(prefix[-1]-prefix[i])//(len(nums)-i-1))<val:
                ans = i
                val = abs(prefix[i]//(i+1)-(prefix[-1]-prefix[i])//(len(nums)-i-1))
        if prefix[-1]//len(nums)<val:
            ans = len(nums)-1
        return ans
            