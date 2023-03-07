class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,r = 0,max(time)*(totalTrips//len(time)+1)
        def colculateTrip(mid):
            trip = 0
            for t in time:
                trip+=mid//t
            return trip
              
        while l<=r:
            mid = (l+r)//2
            if colculateTrip(mid)>=totalTrips:
                r = mid-1
            else:
                l = mid+1
        return l
        
         
        