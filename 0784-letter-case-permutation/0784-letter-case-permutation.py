class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def backtrack(i, current):
            if i == len(s):
                answer.append(''.join(current.copy()))
                return
            if not s[i].isdigit():
                current.append(s[i])
                backtrack(i+1,current)
                current.pop()
                current.append(s[i].swapcase())
                backtrack(i+1,current)
                current.pop()
            else:
                current.append(s[i])
                backtrack(i+1, current)
                current.pop()
        backtrack(0,[])
        return answer
            