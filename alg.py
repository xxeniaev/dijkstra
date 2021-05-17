import heapq


class DijkstraSearch:
    def __init__(self, graph):
        self.graph = graph
        self.results = tuple()

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
                    self.results = (cost, path)
                # visit neighbours
                for c, neighbour in self.graph.points[node]:
                    if neighbour not in visited:
                        heapq.heappush(queue, (cost + c, neighbour, path))

    def write_results(self):
        if self.results == tuple():
            f = open("out.txt", "a")
            f.write("N\n")
            f.close()
        else:
            f = open("out.txt", "a")
            f.write("Y\n" + " ".join(map(str, [x+1 for x in self.results[1]])) + "\n" + str(self.results[0]) + "\n")
            print("Y\n" + " ".join(map(str, [x+1 for x in self.results[1]])) + "\n" + str(self.results[0]) + "\n")
            f.close()

