class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i,j = 0,0
        diri,dirj = 0,1
        for inst in instructions:
            if inst == 'G':
                i+=diri
                j+=dirj
            elif inst == 'L':
                diri,dirj = -1*dirj,diri
            else:
                diri,dirj = dirj,-1*diri
        return (i,j) == (0,0) or (diri,dirj) != (0,1) 
                