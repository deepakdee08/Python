import heapq


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w) -> None:
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        min_heap = []
        distances = [float("inf")] * self.V
        distances[src] = 0
        heapq.heappush(min_heap, (0, src))

        while min_heap:
            dist, u = heapq.heappop(min_heap)
            if dist > distances[u]:
                continue
            for v, w in self.graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    heapq.heappush(min_heap, (distances[v], v))
        return distances


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# Example usage:
# g= Graph(5)
# g.add_edge(0,1,4)
# g.add_edge(0,2,8)
# g.add_edge(1,2,1)
# g.add_edge(1,3,2)
# g.add_edge(2,3,3)
# g.add_edge(3,4,7)
# src_vertex = 0
# shortest_distances = g.dijkstra(src_vertex)
# print("shortest distances from vertex", src_vertex,
# "to all other vertices", shortest_distances)