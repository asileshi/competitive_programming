class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        temp = list(str(n))
        temp.sort()
        orig = temp.copy()
        maxx = int(''.join(temp[::-1]))
        for i in range(len(temp)):
            if temp[i]!='0':
                break
        temp[0],temp[i] = temp[i],temp[0]
        start = 2**floor(log2(int(''.join(temp))))
        if n == 1:
            return True
        while start<=maxx:
            digit = list(str(start))
            print(orig,digit)
            digit.sort()
            if digit == orig:
                return True
            start*=2
        return False
            
                           
        
        