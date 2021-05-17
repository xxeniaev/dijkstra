import collections


class Graph:
    def __init__(self, n: int, adj_list):
        self.size = int(n)
        self.points = collections.defaultdict(list)

        for j in range(n):
            for k in range(len(adj_list[j])):
                if adj_list[j][k] != '0' and k % 2 == 0:
                    self.points[int(adj_list[j][k]) - 1].append((int(adj_list[j][k + 1]), int(j)))

    def __str__(self):
        return str(self.points)
