class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for i in range(len(num1)):
            n1+=((ord(num1[i])-ord('0'))*10**(len(num1)-i-1))
        n2 = 0
        for i in range(len(num2)):
            n2+=((ord(num2[i])-ord('0'))*10**(len(num2)-i-1))
        num = n1*n2
        return str(num)
            
        