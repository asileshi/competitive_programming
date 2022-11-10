class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def backtrack(i, current):
            if i == len(s):
                temp = ''.join(current.copy())
                answer.append(temp)
                return
            if s[i].isdigit():
                current.append(s[i])
                backtrack(i+1,current)
                
            else:
                current.append(s[i].lower())
                backtrack(i+1,current)
                current.pop()
                current.append(s[i].upper())
                backtrack(i+1,current)
            current.pop()
                
        backtrack(0,[])
        return answer