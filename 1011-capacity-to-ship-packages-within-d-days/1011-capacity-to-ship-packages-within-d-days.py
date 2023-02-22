class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            day = 1
            tot =0
            for w in weights:
                if tot+w>capacity:
                    tot = 0
                    day+=1
                tot+=w
            return day
        l, r = max(weights), sum(weights)
        ans = inf
        while l<=r:
            mid = (l+r)//2
            if check(mid)<=days:
                ans = min(ans,mid)
                r = mid-1
            else:
                l = mid+1
        return ans
                
                    