from math import inf
import graf_mst


class Node:
    def __init__(self, key=0, colour=0):
        self.key = key
        self.colour = colour

    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, weight):
        self.weight = weight


class AdjacencyList:
    def __init__(self):
        self.adjacency_list = []
        self.dictionary = {}

    def insertVertex(self, vertex):
        if not vertex in self.dictionary.keys():
            self.dictionary[vertex] = len(self.adjacency_list)
            self.adjacency_list.append([])

    def insertEdge(self, vertex1, vertex2, edge=1):
        self.adjacency_list[self.dictionary[vertex1]].append([self.dictionary[vertex2], edge])
        self.adjacency_list[self.dictionary[vertex2]].append([self.dictionary[vertex1], edge])

    def deleteVertex(self, vertex):
        idx = self.dictionary[vertex]
        for i in range(len(self.adjacency_list)):
            for j in range(len(self.adjacency_list[i])):
                if self.adjacency_list[i][j][0] == idx:
                    self.adjacency_list[i].remove([idx, self.adjacency_list[i][j][1]])

            for j in range(len(self.adjacency_list[i])):
                if self.adjacency_list[i][j][0] > idx:
                    self.adjacency_list[i][j][0] -= 1

        del self.adjacency_list[idx]
        del self.dictionary[vertex]

        for vertex_, val in self.dictionary.items():
            if val > idx:
                self.dictionary[vertex_] = val - 1

    def deleteEdge(self, vertex1, vertex2):
        v1 = self.getVertexIdx(vertex1)
        v2 = self.getVertexIdx(vertex2)
        for i in range(len(self.adjacency_list[v1])):
            if self.adjacency_list[v1][i][0] == v2:
                self.adjacency_list[v1].remove([self.adjacency_list[v1][i][0], self.adjacency_list[v1][i][1]])

    def getVertexIdx(self, vertex):
        return self.dictionary[vertex]

    def getVertex(self, vertex_idx):
        for vertex, val in self.dictionary.items():
            if val == vertex_idx:
                return vertex
        return None

    def neighbours(self, vertex_idx):
        return self.adjacency_list[vertex_idx]

    def order(self):
        return len(self.adjacency_list)

    def size(self):
        total = 0
        for x in self.adjacency_list:
            total += len(x)
        return total // 2

    def edges(self):
        result = []
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                result.append([self.getVertex(i).key, self.getVertex(j).key])
        return result


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v.key, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w, end=";")
        print()
    print("-------------------")


def MST(G, vertexes):
    intree = [0] * G.order()
    distance = [inf] * G.order()
    parent = [-1] * G.order()
    mst = AdjacencyList()
    v = 0
    summ = 0
    while v < G.order():
        if intree[v] == 0:
            intree[v] = 1
            for u in G.neighbours(v):
                if distance[v] > u[1]:
                    distance[v] = u[1]
                    parent[v] = u[0]

            if parent[v] != -1 and distance[v] != inf:
                mst.insertVertex(vertexes[v])
                mst.insertVertex(vertexes[parent[v]])
                mst.insertEdge(vertexes[v], vertexes[parent[v]], int(distance[v]))
                intree[parent[v]] = 1
                summ += int(distance[v])

        v += 1
    printGraph(mst)


def test():
    g = AdjacencyList()
    names = ''
    vertexes = []
    for v in graf_mst.graf:
        if v[0] not in names:
            names += v[0]
            vertexes.append(Node(v[0]))
        if v[1] not in names:
            names += v[1]
            vertexes.append(Node(v[1]))

    for x in vertexes:
        g.insertVertex(x)

    for edges in graf_mst.graf:
        g.insertEdge(vertexes[names.index(edges[0])], vertexes[names.index(edges[1])], edges[2])

    MST(g, vertexes)


test()
#print(graf_mst.graf)
