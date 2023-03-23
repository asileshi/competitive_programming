class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        conn = [i for i in range(n)]
        rank = [0 for i in range(n)]
        def find(x):
            if x == conn[x]:
                return x
            conn[x] = find(conn[x])
            return conn[x]
        reden = [0]
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
            else:
                reden[0]+=1
        for x,y in connections:
            union(x,y)
        groups = 0
        for i,com in enumerate(conn):
            if com==i:
                groups+=1
        if groups-1<=reden[0]:
            return groups-1
        
        return -1
                