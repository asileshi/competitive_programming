class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        one = ''.join(stack.copy())
        stack = []
        for c in t:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack) == one
            
        