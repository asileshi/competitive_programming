class Solution:
    def fullJustify(self, words, maxWidth):
        ans, cur, num_of_letters = [], [], 0
        
        
        for l in words:
            if num_of_letters + len(l) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                ans.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [l]
            num_of_letters += len(l)
        return ans + [' '.join(cur).ljust(maxWidth)]