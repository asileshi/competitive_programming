class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(['0000'])
        q = deque([('0000',0)])
        if '0000' in deadends:
            return -1
        while q:
            lock,step = q.popleft()
            if lock == target:
                return step
            for i in range(4):
                back = lock[:i]+str((int(lock[i])+1)%10)+lock[i+1:]
                front = lock[:i]+str((int(lock[i])-1)%10)+lock[i+1:]
                if back not in visited and back not in deadends:
                    q.append((back,step+1))
                    visited.add(back)
                if front not in visited and front not in deadends:
                    q.append((front,step+1))
                    visited.add(front)
                    
         
        return -1
    