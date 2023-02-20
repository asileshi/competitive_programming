class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4,ip6 = True,True
       
        temp1 = queryIP.split('.')
        for q in temp1:
            if not q.isdigit() or (q[0] == '0' and len(q)>1) or not 0<=int(''.join(q))<=255:
                ip4 = False
                break
        temp2 = queryIP.split(':')
        for q in temp2:
            if not 1<=len(q)<=4:
                ip6 = False
                break
            for l in q:
                if not l.isdigit():
                    if not (97<=ord(l)<=102) and not (65<=ord(l)<=70):
                        ip6 = False
                        break
        print(temp1)
        if ip4 and len(temp1) == 4:
            return 'IPv4'
        if ip6 and len(temp2) == 8:
            return 'IPv6'
        return 'Neither'
                
            
        
        
        