class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        one,two = [],[]
        for num in nums:
            if num%3 == 1:
                one.append(num)
            if num%3 == 2:
                two.append(num)
        if total%3 == 1:
            ans = -inf
            if one:
                ans = max(ans,total-min(one))
            if len(two)>1:
                two.sort()
                ans = max(ans,total-two[0]-two[1])
            return ans if ans!=-inf else -1

        elif total%3 == 2:
            ans = -inf
            if two:
                ans = ans = max(ans,total-min(two))
            if len(one)>1:
                one.sort()
                ans = max(ans,total-one[0]-one[1])
            return ans if ans!=-inf else -1
        else:
            return total

