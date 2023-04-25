class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        i = 0
        while i<len(s):
            stack.append(s[i])
            if len(stack)>=len(part):
                temp = ''.join(stack[-len(part):])
                if temp == part:
                    for l in part:
                        stack.pop()
            i+=1
        return ''.join(stack)