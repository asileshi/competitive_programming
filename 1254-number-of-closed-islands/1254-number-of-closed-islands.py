class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans =0
        dirr = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited:
                    temp = [(i,j)]
                    flag = 0
                    while temp:
                        cur = temp.pop()
                        visited.add(cur)
                        for d in dirr:
                            newi,newj = d[0]+cur[0],d[1]+cur[1]
                            if newi<0 or newi>=len(grid) or newj<0 or newj>=len(grid[0]):
                                flag =1
                            elif grid[newi][newj] == 0 and (newi,newj) not in visited:
                                temp.append((newi,newj))
                    if flag == 0:
                        ans+=1
        return ans
                            
        