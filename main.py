from reader import ReadFromFile as Reader
from graph import Graph
from alg import Finder

if __name__ == '__main__':
    reader = Reader("in.txt")

    params = reader.reading()
    print('params: ', params)

    f = open("out.txt", "w")
    f.close()

    print('тут0')
    graph = Graph(params[0], params[1])
    print('тут1')
    print(graph.points)
    finder = Finder(graph)
    # checker.dfs(1, 1)
    # checker.print_results()
    print("Find the shortest path with Dijkstra")
    print(graph.points)
    print("1 -> 3:")
    print(finder.shortest_path(params[2], params[3]))
