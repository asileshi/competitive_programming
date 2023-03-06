class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        st = set(arr)
        i = 1
        while k>0:
            if i not in st:
                k-=1
            i+=1
        return i-1