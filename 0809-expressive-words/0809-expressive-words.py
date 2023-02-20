class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count(s):
            count = []
            i = 0
            while i<len(s):
                j,temp = i,0
                while j<len(s) and s[j] == s[i]:
                    temp+=1
                    j+=1
                count.append([s[i],temp])
                i = j
            return count
        s_count = count(s)
        ans = 0
        for st in words:
            temp = count(st)
            if len(s_count) == len(temp):
                state = True
                for i in range(len(temp)):
                    if temp[i][0]!=s_count[i][0] or temp[i][1]>s_count[i][1] or (s_count[i][1]<3 and s_count[i][1]!=temp[i][1]):
                            state = False
                            break
                if state:
                    ans+=1
        return ans
        