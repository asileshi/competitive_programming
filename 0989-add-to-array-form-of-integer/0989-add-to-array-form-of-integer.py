class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = [str(i) for i in num]
        summ = int(''.join(temp))+k
        return [int(i) for i in list(str(summ))]
        