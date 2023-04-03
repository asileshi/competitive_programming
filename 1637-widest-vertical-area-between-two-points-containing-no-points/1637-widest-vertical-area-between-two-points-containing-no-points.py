class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        area = 0
        for i,(x,y) in enumerate(points):
            area = max(area,x-points[i-1][0])
        return area