class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        orginal = defaultdict(int)
        for l in p:
            orginal[l]+=1
        ans = []
        l,count = 0,0
        temp = defaultdict(int)
        for i in range(len(s)):
            temp[s[i]]+=1
            count+=1
            while temp[s[i]]>orginal[s[i]] or count>len(p):
                temp[s[l]]-=1
                count-=1
                l+=1 
            if temp[s[i]] == orginal[s[i]] and count == len(p):
                ans.append(l)
        return ans