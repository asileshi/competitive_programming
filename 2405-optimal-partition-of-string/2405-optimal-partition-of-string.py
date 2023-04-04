class Solution:
    def partitionString(self, s: str) -> int:
        st = set()
        l = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in st:
                ans+=1
                st = set([s[i]])
            else:
                st.add(s[i])
        return ans+1
                    
        