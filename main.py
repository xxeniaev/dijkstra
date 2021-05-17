from reader import ReadFromFile as Reader
from graph import Graph
from alg import DijkstraSearch

if __name__ == '__main__':
    reader = Reader("in.txt")

    params = reader.reading()

    f = open("out.txt", "w")
    f.close()

    graph = Graph(params[0], params[1])
    searcher = DijkstraSearch(graph)
    print("Find the shortest path with Dijkstra")
    print("1 -> 4:")
    print('res0: ', searcher.results)
    searcher.shortest_path(params[2]-1, params[3]-1)
    print('res1: ', searcher.results)
    searcher.write_results()
