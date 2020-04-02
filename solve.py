from sys import argv
from maze import *

if __name__ == "__main__":
    assert len(argv) == 4, "requires method, old, new"

    _, method, old, new = argv
    m = maze(old)

    if method == "Astar":
        from Astar import *
        Astar(m.graph, m.start, m.end)
    elif method == "BFS":
        from BFS import *
        BFS(m.graph, m.start, m.end)
    elif method == "DFS":
        from DFS import *
        DFS(m.graph, m.start, m.end)
    elif method == "Dijkstra":
        from Dijkstra import *
        Dijkstra(m.graph, m.start, m.end)
    else:
        raise ValueError("no solver found")

    m.path = reconstruct(m.graph, m.end)
    m.setpath()
    m.save(new)