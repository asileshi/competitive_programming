class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char = {}
        mapedto = {}
        for i in range(len(s)):
            if s[i] in char and char[s[i]]!=t[i]:
                return False
            else:
                if t[i] in mapedto and mapedto[t[i]]!=s[i]:
                    return False
                char[s[i]] = t[i]
                mapedto[t[i]] = s[i]
                
        return True
        
        