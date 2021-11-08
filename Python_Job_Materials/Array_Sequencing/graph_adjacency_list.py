#               Vertex - (circles)
# vertex (also called a "node") is a fundamentl part of a graph
# it can have a name, which we will call the "key"
# a vertex may also have additional information
# we will call this additional information the "payload"

#               Edge
# edge connects two vertices to show that there is a relationship between them
# edges may be one-way or two-way
# if the edges in a graph are all one-way, we say that the graph is a *directed graph* or *digraph*
# the class prerequisites graphs shown previously is clearly a digraph since you must take some before others

#               Weight
# edges may be weighted to show that there is a cost to go from one vertex to another
# for example in a graph of roads that connect one city to another, the weight on the 
# edge might represent the distance between the two cites


class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]



class Graph:
    def __init__(self):
        self.vertList = {}  # called a list, but actually a dictionary
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# //

g = Graph()

for i in range(6): 
    g.addVertex(i)

print(g.vertList)

g.addEdge(0, 1, 2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')
