class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        temp,l,ans,count = defaultdict(int),0,0,0
        for i in range(len(fruits)):
            if temp[fruits[i]] == 0:
                count+=1
            temp[fruits[i]]+=1
            while count>2:
                temp[fruits[l]]-=1
                if temp[fruits[l]] == 0:
                    count-=1
                l+=1
            ans = max(ans,i-l+1)
        return ans
                
            
            