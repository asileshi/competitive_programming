class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        conn = [i for i in range(len(source))]
        rank = [0]*len(source)
        def find(x):
            if x == conn[x]:
                return x
            conn[x] = find(conn[x])
            return conn[x]
        def union(x,y):
            rootx,rooty = find(x),find(y)
            if rootx!=rooty:
                if rank[rootx]>rank[rooty]:
                    conn[rooty] = rootx
                elif rank[rootx]<rank[rooty]:
                    conn[rootx] = rooty
                else:
                    conn[rootx] = rooty
                    rank[rooty]+=1
        for x,y in allowedSwaps:
            union(x,y)
        hmap = defaultdict(list)
        for i in range(len(conn)):
            find(i)
            hmap[conn[i]].append(i)
        ans = 0
        for n in hmap:
            temp = defaultdict(int)
            for idx in hmap[n]:
                temp[source[idx]]+=1
            for idx in hmap[n]:
                if temp[target[idx]] == 0:
                    ans+=1
                else:
                    temp[target[idx]]-=1
        return ans
                    