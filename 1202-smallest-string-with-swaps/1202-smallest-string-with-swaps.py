class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        idx = defaultdict(list)
        rank = [0]*len(s)
        conn = [i for i in range(len(s))]
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
        for x,y in pairs:
            union(x,y)
        for i,num in enumerate(conn):
            find(i)
            idx[conn[i]].append(i)
        new = list(s)
        for n in idx:
            temp = [new[i] for i in idx[n]]
            temp.sort()
            i = 0
            while i<len(temp):
                new[idx[n][i]] = temp[i]
                i+=1
        return ''.join(new)
                    
        
        