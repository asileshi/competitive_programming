class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = []
        self.l,self.r = 0,-1

    def enQueue(self, value: int) -> bool:
        if self.r-self.l+1<self.k:
            self.q.append(value)
            self.r+=1
            return True
        return False
    def deQueue(self) -> bool:
        if self.r-self.l>=0:
            self.l+=1
            return True
        return False
        
    def Front(self) -> int:
        if self.r-self.l>=0:
            return self.q[self.l]
        return -1
        
    def Rear(self) -> int:
        if self.r-self.l>=0:
            return self.q[-1]
        return -1
        
    def isEmpty(self) -> bool:
        return self.r-self.l<0
        
    def isFull(self) -> bool:
        return self.r-self.l+1 == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()