from sys import argv
from Methods import *
from maze import *

if __name__ == "__main__":
    assert len(argv) == 4, "requires method, old, new"

    _, method, old, new = argv
    m = maze(old)

    if method == "Astar":
        Astar.Astar(m.graph, m.start, m.end)
    elif method == "BFS":
        BFS.BFS(m.graph, m.start, m.end)
    elif method == "DFS":
        DFS.DFS(m.graph, m.start, m.end)
    elif method == "Dijkstra":
        Dijkstra.Dijkstra(m.graph, m.start, m.end)
    else:
        raise ValueError("no method found")

    m.path = reconstruct(m.graph, m.end)
    m.setpath()
    m.save(new)