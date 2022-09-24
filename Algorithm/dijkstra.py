import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)]
                        for row in range(vertices)]

    def print(self, dist):
        print("Vertices \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def min_distance(self, dist, sptSet):

        mindis = sys.maxsize
        min_index = None
        for u in range(self.V):
            
            if dist[u] < mindis and sptSet[u] == False:
                mindis = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):

            x = self.min_distance(dist, sptSet)

            sptSet[x] = True

            for y in range(self.V):

                if self.graph[x][y] > 0 and sptSet[y] == False and \
                    dist[y] > dist[x] + self.graph[x][y]:

                    dist[y] = dist[x] + self.graph[x][y]

        self.print(dist)


if __name__ == '__main__':

    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    g.dijkstra(0)