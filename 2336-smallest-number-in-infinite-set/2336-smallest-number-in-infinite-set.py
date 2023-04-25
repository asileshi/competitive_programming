class SmallestInfiniteSet:

    def __init__(self):
        self.minn = 1
        self.st = set()
        

    def popSmallest(self) -> int:
        self.st.add(self.minn)
        temp = self.minn
        while self.minn in self.st:
            self.minn+=1
        return temp
    def addBack(self, num: int) -> None:
        if num in self.st:
            self.st.remove(num)
        if num<self.minn:
            self.minn = num

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)