from PIL import Image
from graph import *

class maze:
    def __init__(self, filename):
        self.start = None
        self.end = None
        self.graph = graph()
        self.graph.path = []
        self.load(filename)
    
    def load(self, filename):
        self.filename = filename
        self.im = Image.open(filename)
        width, height = self.im.size
        data = list(self.im.getdata(0))
        f = lambda x,y: data[y*width+x]

        prevline = [None] * width
        for x in range(1, width - 1): #start row
            if f(x, 0):
                self.start = self.graph.addvertex(x, 0)
                prevline[x] = self.start
                break
        
        for y in range(1, height - 1):
            prev = None
            for x in range(1, width - 1):
                if f(x, y):
                    if f(x+1, y) != f(x-1, y) or f(x, y+1) != f(x, y-1) or (f(x+1, y) and f(x-1, y) and f(x, y+1) and f(x, y-1)):
                        cur = self.graph.addvertex(x, y)
                        if prev != None:
                                cur.edges[3] = prev
                                prev.edges[1] = cur
                        
                        if prevline[x] != None:
                                cur.edges[2] = prevline[x]
                                prevline[x].edges[0] = cur
                        
                        prev = cur
                        prevline[x] = cur
                else:
                    prev = None
                    prevline[x] = None

        for x in range(1, width - 1): #end row
            if f(x, height-1):
                self.end = self.graph.addvertex(x, height - 1)
                self.end.edges[2] = prevline[x]
                prevline[x].edges[0] = self.end
                break
    
    def setpath(self, start_colour = [255,0,0], end_colour = [0,0,255]):
        colour = end_colour
        inc = [(s-e)/(len(self.path)-1) for s,e in zip(start_colour,end_colour)]
        for c in self.path:
            self.im.putpixel(c, tuple(int(v) for v in colour))
            colour = [c+i for c,i in zip(colour,inc)]
    
    def show_vertecies(self):
        im = self.im.copy()
        for v in self.graph.vertices:
            im.putpixel((v.x, v.y), (0, 255, 0))
        im.save(self.filename[:-4] + "_new" + self.filename[-4:])

    def save(self, filename = None):
        if filename == None:
            self.im.save(self.filename[:-4] + "_new" + self.filename[-4:])
        else:
            self.im.save(filename)