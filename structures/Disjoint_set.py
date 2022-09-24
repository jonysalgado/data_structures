

class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    # The find function here is the same as that in the disjoint set with path compression.
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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def __len__(self):
        return len(self.root)

    def __repr__(self):
        sets = {}
        for i in range(len(self.root)):
            sets[self.find(i)] = sets.get(self.find(i), []) + [str(i)]

        repr = ''
        for i in sets.keys():
            repr += '[' + ','.join(sets[i]) + ']'
            repr += ' '

        return repr

if __name__ == '__main__':

    uf = DisjointSet(10)
    print(uf)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    print(uf)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    print(uf)
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf)