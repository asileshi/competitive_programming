class DetectSquares:

    def __init__(self):
        self.hash_map = defaultdict(int)
        self.cord = []
    def add(self, point: List[int]) -> None:
        self.hash_map[(point[0],point[1])]+=1
        self.cord.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        for pnt in self.cord:
            if abs(pnt[1]-point[1]) != abs(pnt[0]-point[0]) or pnt[0] == point[0] or pnt[1] == point[1]:
                continue
            ans+=self.hash_map[(pnt[0],point[1])]*self.hash_map[(point[0],pnt[1])]
        return ans
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)