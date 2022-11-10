class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            temp = {}
            for j in range(len(points)):
                denom = points[j][0]-points[i][0]
                if i!=j and denom != 0:
                    slope = (points[j][1] -points[i][1])/denom
                    if slope in temp:
                        temp[slope]+=1
                        ans = max(ans,temp[slope])
                    else:
                        temp[slope] = 2
                        ans = max(ans,temp[slope])
                if i!=j and denom == 0:
                    if "v" in temp:
                        temp["v"]+=1
                        ans = max(ans,temp["v"])
                    else:
                        temp["v"]=2
                        ans = max(ans,temp["v"])
        return ans
                    