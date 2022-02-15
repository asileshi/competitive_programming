class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = ""
        temp=""
        for j in range(n):
            if j==0:
                ans+="0"
            else:
                temp = ""
                for i in range(len(ans)):
                    if ans[i]=="0":
                        temp+="1"
                    elif ans[i]=="1":
                        temp+="0"
                temp=temp[::-1]
                ans+="1"+temp
        return ans[k-1]
