class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for l in s:
            if stack and stack[-1][0] == l:
                if stack[-1][1] == k-1:
                    for i in range(k-1):
                        stack.pop()
                else:
                    stack.append([l,stack[-1][1]+1])
            else:
                stack.append([l,1])
        return ''.join([l[0] for l in stack])