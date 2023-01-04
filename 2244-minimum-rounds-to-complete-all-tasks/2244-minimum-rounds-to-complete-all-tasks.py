class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task]+=1
        ans = 0
        for i in count:
            if count[i]%3 == 0:
                ans+=count[i]//3
            elif count[i] == 2:
                ans+=1
            elif count[i]%3 == 2:
                ans+=count[i]//3+1
            elif count[i]-4>=0:
                ans+=(count[i]-4)//3+2
            else:
                return -1
        return ans
                    