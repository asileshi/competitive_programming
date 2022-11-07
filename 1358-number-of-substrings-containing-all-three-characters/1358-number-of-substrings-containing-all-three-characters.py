class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = defaultdict(int)
        answer = 0
        l = 0
        for i in range(len(s)):
            abc[s[i]]+=1
            while len(abc)==3:
                answer+=(len(s)-i)
                abc[s[l]]-=1
                if abc[s[l]] == 0:
                    del abc[s[l]]
                l+=1
        return answer
        