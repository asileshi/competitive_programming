class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for l in s:
            d[l]+=1
        heap = []
        ans = []
        for l in d:
            heappush(heap,[-d[l],l])
        while heap:
            high = heappop(heap)
            if heap:
                low = heappop(heap)
                ans.append(high[1])
                high[0]+=1
                if high[0]<0:
                    heappush(heap,high)
                ans.append(low[1])
                low[0]+=1
                if low[0]<0:
                    heappush(heap,low)
            else:
                if high[0]==-1:
                    ans.append(high[1])
                else:
                    return ''
        return ''.join(ans)
                