class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        duplicate = 0
        for i in nums:
            count[i]+=1
            if count[i] == 2:
                duplicate = i
        for i in range(1,len(nums)+1):
            if i not in count:
                break
        return [duplicate,i]
        