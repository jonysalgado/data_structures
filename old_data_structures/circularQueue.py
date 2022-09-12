class MyCircularQueue:

    def __init__(self, k: int):
        self.values = [None for _ in range(k)]
        self.k = k
        self.first = None
        self.last = None

    def enQueue(self, value: int) -> bool:
        n = self.last
        if n is None:
            self.values[0] = value
            self.first = self.last = 0
            return True
        elif self.isFull():
            return False
        else:
            self.values[(n + 1)%self.k] = value
            self.last = (n + 1)%self.k
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.last == self.first:
            self.values[self.first] = None
            self.last = self.first = None
            return True
        
        n = self.first
        self.values[n] = None
        self.first = (n + 1)%self.k
        return True
        
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.values[self.first]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.values[self.last]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.first == self.last == None:
            return True
        return False

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        n = self.last
        if (n + 1)%self.k == self.first:
            return True
            
        return False