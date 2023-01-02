class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        for i in word:
            if i.isupper():
                capital+=1
        if len(word) == capital or capital == 0:
            return True
        if capital == 1:
            return word[0].isupper()
        return False