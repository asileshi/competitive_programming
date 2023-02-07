class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log[0:len(log)-1] == '..':
                if stack:
                    stack.pop()
                
            elif log[0:len(log)-1] == '.':
                pass
            else:
                stack.append(log[0:len(log)-1])
        return len(stack)