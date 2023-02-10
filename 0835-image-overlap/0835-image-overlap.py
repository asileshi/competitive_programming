class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        temp1,temp2 = [],[]
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    temp1.append((i, j))
        
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1:
                    temp2.append((i, j))
        
        hmap = defaultdict(int)
        for x1, y1 in temp1:
            for x2, y2 in temp2:
                hmap[(x1 - x2, y1 - y2)] += 1
        return max(hmap.values()) if len(hmap.values()) else 0
        
    