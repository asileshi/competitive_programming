class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        intersecting = abs(ax1-ax2)*abs(ay1-ay2)+abs(bx1-bx2)*abs(by1-by2)
        cordx = [(ax1,ax2),(bx1,bx2)]
        cordx.sort()
        cordy = [(ay1,ay2),(by1,by2)]
        cordy.sort()
        cx = -1
        if cordx[1][1]>=cordx[0][1]:
            cx = cordx[0][1]-cordx[1][0]
        else:
            cx = cordx[1][1]-cordx[1][0]
        cy = -1
        if cordy[1][1]>=cordy[0][1]:
            cy = cordy[0][1]-cordy[1][0]
        else:
            cy = cordy[1][1]-cordy[1][0]
        if cx>0 and cy>0:
            return intersecting-(cy*cx)
        else:
            return intersecting