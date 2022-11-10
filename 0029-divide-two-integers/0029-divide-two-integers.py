class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        negative = (dividend<0)^(divisor<0)
        dividend,divisor= abs(dividend),abs(divisor)
        start = divisor
        while dividend>=divisor:
            temp = 1
            while dividend>=divisor<<1:
                temp<<=1
                divisor<<=1
            ans+=temp
            dividend = dividend-divisor
            divisor = start
        if negative:
            ans*=-1
        if ans>2**31-1:
            return 2**31-1
        if ans<-2**31:
            return -2**31
        return ans