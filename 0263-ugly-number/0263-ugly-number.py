class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        arr = []
        def primeFactors(n):

            while n % 2 == 0:
                arr.append(2),
                n = n / 2

          
            for i in range(3,int(math.sqrt(n))+1,2):

                while n % i== 0:
                    arr.append(i),
                    n = n / i

            if n > 2:
                arr.append(n)
        primeFactors(n)
        for i in arr:
            if not(i==2 or i==3 or i==5):
                return False
        return True
         
