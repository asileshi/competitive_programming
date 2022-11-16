class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = i = 0
        while i<len(plants):
            temp = capacity
            while i<len(plants) and temp>=plants[i]:
                ans+=1
                temp-=plants[i]
                i+=1
            if i < len(plants):
                ans+=2*i
        return ans