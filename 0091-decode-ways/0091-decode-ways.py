class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        table = [0 for _ in range(len(s)+1)]
        table[0] = 1
        for i in range(1,len(table)):
            if s[i-1]!='0':
                table[i] += table[i-1]
            if i>=2:
                if 10<=int(s[i-2:i])<=26:
                    table[i]+=table[i-2]
        return table[-1]