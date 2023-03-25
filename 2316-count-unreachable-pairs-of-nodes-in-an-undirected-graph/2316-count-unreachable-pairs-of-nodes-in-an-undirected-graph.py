class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        conn = [i for i in range(n)]
        rank = [0]*n
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
        for x,y in edges:
            union(x,y)
        count = defaultdict(int)
        tot = n
        for i in range(len(conn)):
            find(i)
            count[conn[i]]+=1
        ans = 0
        for c in count:
            tot-=count[c]
            ans+=(tot*count[c])
        return ans
            
        