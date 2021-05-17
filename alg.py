import collections
import heapq


class Finder:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, source, sink):
        # create a priority queue and hash set to store visited nodes
        queue, visited = [(0, source, [])], set()
        heapq.heapify(queue)
        # traverse graph with BFS
        while queue:
            (cost, node, path) = heapq.heappop(queue)
            # visit the node if it was not visited before
            if node not in visited:
                visited.add(node)
                path = path + [node]
                # hit the sink
                if node == sink:
                    return (cost, path)
                # visit neighbours
                for c, neighbour in self.graph.points[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost + c, neighbour, path))
        return float("inf")

    def print_results(self):
        pass
