from reader import ReadFromFile as Reader
from graph import Graph
from alg import Finder

if __name__ == '__main__':
    reader = Reader("in.txt")

    params = reader.reading()

    f = open("out.txt", "w")
    f.close()

    graph = Graph(params[0], params[1])
    finder = Finder(graph)
    print("Find the shortest path with Dijkstra")
    print("1 -> 3:")
    print(finder.shortest_path(params[2]-1, params[3]-1))
