class Solution:
    def racecar(self, target: int) -> int:
        visited = set()
        q = deque([(0,0,1)])
        while q:
            front = q.popleft()
            if front[1] == target:
                return front[0]
            elif (front[1],front[2]) not in visited:
                visited.add((front[1],front[2]))
                q.append((front[0]+1,front[1]+front[2],front[2]*2))
                if (front[1]+front[2]>target and front[2]>0) or (front[1]+front[2]<target and front[2]<0):
                        if front[2]>0:
                            q.append((front[0]+1,front[1],-1)) 
                        else:
                            q.append((front[0]+1,front[1],1)) 
                    