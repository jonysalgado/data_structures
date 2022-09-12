from typing import List
import unittest

def earliestAcq(logs: List[List[int]], n: int) -> int:
        
    logs = sorted(logs, key=lambda x: x[0])
    ds = DisjoinSet(n)
    for log in logs:
        
        ds.union(log[1], log[2])
        
        if ds.groups == 1:
            return log[0]
        
    return -1
        
        
        
class DisjoinSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.groups = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            
            self.groups -= 1

class Test(unittest.TestCase):
    test_cases = [
        ([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6, 20190301),
        ([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4, 3)
    ]

    test_functions = [earliestAcq]

if __name__ == "__main__":
    unittest.main()


