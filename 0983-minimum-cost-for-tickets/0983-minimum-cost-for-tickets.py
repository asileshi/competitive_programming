class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ans = [inf]*(len(days)+1)
        ans[0] = 0
        for i,d in enumerate(days):
            if ans[i]!=inf:
                one = bisect.bisect_left(days,d+1)
                seven = bisect.bisect_left(days,d+7)
                thirty = bisect.bisect_left(days,d+30)
                if one <len(ans):
                    ans[one] = min(ans[one],ans[i]+costs[0])
                else:
                    ans[one-1] = min(ans[one-1],ans[i]+costs[0])
                if seven < len(ans):
                    ans[seven] = min(ans[seven],ans[i]+costs[1])
                else:
                    ans[seven-1] = min(ans[seven-1],ans[i]+costs[1])
                if thirty <len(ans):
                    ans[thirty] = min(ans[thirty],ans[i]+costs[2])
                else:
                    ans[thirty-1] = min(ans[thirty-1],ans[i]+costs[2])
        return ans[-1]
                    
        
        