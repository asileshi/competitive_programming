class Solution:
    def kClosest(self, points, k):
        closest = []
        for i in points:
            x = i[0] ** 2 + i[1] ** 2
            closest.append([x,i[0],i[1]])
        closest.sort()
        for j in closest:
            j.pop(0)
        return closest[0:k]