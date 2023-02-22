class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        temp = list(s)
        ans = 0
        while True:
            found = 0
            i = 0
            while i<len(temp):
                if i+1<len(temp) and temp[i] == '0' and temp[i+1] == '1':
                    temp[i],temp[i+1] = temp[i+1],temp[i]
                    found+=1
                    i+=2
                else:
                    i+=1
            if found > 0:
                ans+=1
            else:
                break
        return ans
                    