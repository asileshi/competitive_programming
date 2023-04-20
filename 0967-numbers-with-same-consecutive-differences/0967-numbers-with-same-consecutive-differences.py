class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtrack(temp,l):
            if l==0:
                if len(temp) == n:
                    ans.append(int(''.join(temp.copy())))
                return 
            if temp:
                if int(temp[-1])>=k:
                    if int(temp[-1])+k<10:
                        temp.append(str(int(temp[-1])+k))
                        backtrack(temp,l-1)
                        temp.pop()
                    if int(temp[-1])-k>=0:
                        temp.append(str(int(temp[-1])-k))
                        backtrack(temp,l-1)
                        temp.pop()
                else:
                    if int(temp[-1])+k<10:
                        temp.append(str(int(temp[-1])+k))
                        backtrack(temp,l-1)
                        temp.pop()
            else:
                for i in range(1,10):
                    temp.append(str(i))
                    backtrack(temp,l-1)
                    temp.pop()
        backtrack([],n)
        return set(ans)
                    
                    