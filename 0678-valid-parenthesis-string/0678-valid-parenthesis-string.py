class Solution(object):
    def checkValidString(self, s):
        o,c = 0,0
        for ch in s:
            if ch == '(':
                o+=1
            else:
                o-=1
            if ch != ')':
                c+=1
            else:
                c-=1
            
            if c < 0: break
            o = max(o, 0)

        return o == 0