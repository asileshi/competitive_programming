class Solution:
    def addDigits(self, num: int) -> int:
        def calc(num):
            if len(str(num))==1:
                return num
            temp = 0
            for d in str(num):
                temp+=int(d)
            return calc(temp)
        return calc(num)
        