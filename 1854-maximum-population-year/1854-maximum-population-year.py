class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        minn,maxx = inf,0
        for log in logs:
            minn,maxx = min(minn,log[0]),max(maxx,log[1])
            count = 0
            ans = 0
        for year in range(minn,maxx+1):
            temp = 0
            for log in logs:
                if log[0]<=year<log[1]:
                    temp+=1
            if temp>count:
                count = temp
                ans = year
        return ans
                    
            