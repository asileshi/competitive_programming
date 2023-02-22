class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timeCount = defaultdict(int)
        for t in time:
            timeCount[t%60]+=1
        ans = 0
        for t in time:
            timeCount[t%60]-=1
            diff = 60-t%60
            if diff == 60:
                ans+=timeCount[0]
            else:
                ans+=timeCount[diff]
        return ans