class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0
        for i in range(len(bin(num))-2):
            if num&(2**i) == 0:
                answer+=2**i
        return answer
                
        