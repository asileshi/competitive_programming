class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(temp,op,tot):
            if tot==0:
                if op == 0:
                    ans.append(temp)
                return
            if op>0:
                backtrack(temp+[')'],op-1,tot-1)
            backtrack(temp+['('],op+1,tot-1)
        backtrack([],0,2*n)
        return [''.join(i) for i in ans]
        
            