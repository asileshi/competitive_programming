class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q,l = deque(),0
        for i in range(k):
            if not q:
                q.append(i)
            else:
                while q and nums[q[-1]]<=nums[i]:
                    q.pop()
                q.append(i)
        ans = []
        for i in range(k,len(nums)):
            ans.append(nums[q[0]])
            l+=1
            if q[0]<l:
                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
        if q :
            ans.append(nums[q[0]])
        return ans
            