from queue import Queue

def BFS(G, start, end):
    for v in G.vertices:
        v.discovered = False
    
    Q = Queue()
    start.discovered = True
    Q.put(start)
    while not Q.empty():
        v = Q.get()
        
        if v == end:
            return True
        
        for edge in v.edges:
            if edge != None and not edge.discovered:
                edge.discovered = True
                edge.prev = v
                Q.put(edge)
    
    return False