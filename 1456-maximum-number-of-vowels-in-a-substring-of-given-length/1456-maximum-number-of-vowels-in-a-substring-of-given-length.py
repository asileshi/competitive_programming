class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        st = set(['a','e','i','o','u'])
        l = 0
        vowel = size = ans = 0
        for i in range(len(s)):
            if s[i] in st:
                vowel+=1
            size+=1
            while size>k:
                if s[l] in st:
                    vowel-=1
                size-=1
                l+=1
            ans = max(ans,vowel)
        return ans
        