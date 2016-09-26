import random
from copy import deepcopy

data =open("kargerMinCut.txt","r")
Graph={}

for line in data:
    edges = [int(s) for s in line.split()]
    Graph[edges[0]] = edges[1:]

#Random Contraction Algorithm

def kargerContraction(Graph):
    random.seed()
    vertex1,vertex2=chooseRandomVertex(Graph)
    newVetex = mergeVertices(vertex1,vertex2,Graph)
    removeSelfLoops(newVetex)

#Choose random vertices, such that both vertices are not same.

def chooseRandomVertex(Graph):
    vertex1 = random.randint(0, len(Graph)-1)
    vertex2 = random.randint(0, len(Graph)-1)
    #i=1
    while(vertex2==vertex1):
        vertex2 = random.randint(0, len(Graph)-1)

    return vertex1,vertex2

# Merge the randomly chosen vertices

def mergeVertices(vertex1,vertex2,Graph):
    #print(vertex1)
    #print(vertex2)
    #print(len(Graph))
    vertices = list(Graph.keys())
    Graph[vertices[vertex1]].extend(Graph[vertices[vertex2]])

    for i in Graph:
        Graph[i]=[vertices[vertex1] if x==vertices[vertex2] else x for x in Graph[i]]

    del Graph[vertices[vertex2]]
    #print(Graph)
    return vertices[vertex1]


# remove self loops with in the merged vertex

def removeSelfLoops(newVetex):

    Graph[newVetex]=[x for x in Graph[newVetex] if x!=newVetex]
    return Graph

# merging the whole graph to two vertices

def kargerAlgorithm(Graph):
    while len(Graph)>2:
        kargerContraction(Graph)
    return len(Graph[list(Graph.keys())[0]])

#print(kargerAlgorithm(Graph))

# normalizing the data to find the optimum cut value

def findMin_Cut(Graph,n):
    i=0
    count= 10000
    while i<n:
        datacopy = deepcopy(Graph)
        min_cut = kargerAlgorithm(datacopy)
        if min_cut < count:
            count= min_cut
        i = i+1
    return count

print(findMin_Cut(Graph,200))




#print(Graph)
#print(len(Graph[1]))
