class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            minn = 0
            for j in range(len(strs)):
                cur = ord(strs[j][i])
                if cur<minn:
                    ans+=1
                    break
                minn = max(minn,cur)
        return ans