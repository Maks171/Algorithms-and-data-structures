import polska
class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:   return True
        return False

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self):
        pass


class AdjacencyList:
    def __init__(self):
        self.adjacency_list = []
        self.dictionary = {}

    def insertVertex(self, vertex):
        self.dictionary[vertex] = len(self.adjacency_list)
        self.adjacency_list.append([])

    def insertEdge(self, vertex1, vertex2, edge=1):
        self.adjacency_list[self.dictionary[vertex1]].append(self.dictionary[vertex2])

    def deleteVertex(self, vertex):
        idx = self.dictionary[vertex]
        for i in range(len(self.adjacency_list)):
            if idx in self.adjacency_list[i]:
                self.adjacency_list[i].remove(idx)

            for j in range(len(self.adjacency_list[i])):
                if self.adjacency_list[i][j] > idx:
                    self.adjacency_list[i][j] -= 1

        del self.adjacency_list[idx]
        del self.dictionary[vertex]

        for vertex_, val in self.dictionary.items():
            if val > idx:
                self.dictionary[vertex_] = val - 1

    def deleteEdge(self, vertex1, vertex2):
        self.adjacency_list[self.dictionary[vertex1]].remove(self.dictionary[vertex2])

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
        a = self.adjacency_list
        result = []
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                result.append([self.getVertex(i).key, self.getVertex(j).key])
        return result


class AdjacencyMatrix:
    def __init__(self):
        self.adjacency_matrix = []
        self.dictionary = {}

    def insertVertex(self, vertex):
        self.dictionary[vertex] = len(self.adjacency_matrix)
        for i in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[i].append(0)
        self.adjacency_matrix.append([0] * (len(self.adjacency_matrix) + 1))

    def insertEdge(self, vertex1, vertex2, edge=1):
        self.adjacency_matrix[self.dictionary[vertex1]][self.dictionary[vertex2]] = 1

    def deleteVertex(self, vertex):
        idx = self.dictionary[vertex]
        for i in range(len(self.adjacency_matrix)):
            if i == idx:
                continue
            for j in range(idx + 1, len(self.adjacency_matrix[i])):
                self.adjacency_matrix[i][j - 1] = self.adjacency_matrix[i][j]
            self.adjacency_matrix[i].pop()

        del self.adjacency_matrix[idx]
        del self.dictionary[vertex]

        for vertex_, val in self.dictionary.items():
            if val > idx:
                self.dictionary[vertex_] = val - 1

    def deleteEdge(self, vertex1, vertex2):
        self.adjacency_matrix[self.dictionary[vertex1]][self.dictionary[vertex2]] = 0

    def getVertexIdx(self, vertex):
        return self.dictionary[vertex]

    def getVertex(self, vertex_idx):
        for vertex, val in self.dictionary.items():
            if val == vertex_idx:
                return vertex
        return None

    def neighbours(self, vertex_idx):
        result = []
        for i in range(len(self.adjacency_matrix[vertex_idx])):
            if self.adjacency_matrix[vertex_idx][i]:
                result.append(i)
        return result

    def order(self):
        return len(self.adjacency_matrix)

    def size(self):
        total = 0
        for i in self.adjacency_matrix:
            total += sum(i)
        return total // 2

    def edges(self):
        result = []
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix[i])):
                if self.adjacency_matrix[i][j]:
                    result.append([self.getVertex(i).key, self.getVertex(j).key])
        return result


def test_list():
    G_lis = AdjacencyList()
    names = 'ZGNFPCWBETLDOSKR'
    vertexes = []
    for i in range(16):
        vertexes.append(Node(names[i]))
        G_lis.insertVertex(vertexes[i])

    for x in polska.graf:
        G_lis.insertEdge(vertexes[names.index(x[0])], vertexes[names.index(x[1])])

    G_lis.deleteVertex(vertexes[names.index('K')])
    G_lis.deleteEdge(vertexes[names.index('E')], vertexes[names.index('W')])
    G_lis.deleteEdge(vertexes[names.index('W')], vertexes[names.index('E')])
    polska.draw_map(G_lis.edges())


def test_matrix():
    G_matrix = AdjacencyMatrix()
    names = 'ZGNFPCWBETLDOSKR'
    vertexes = []
    for i in range(16):
        vertexes.append(Node(names[i]))
        G_matrix.insertVertex(vertexes[i])

    for x in polska.graf:
        G_matrix.insertEdge(vertexes[names.index(x[0])], vertexes[names.index(x[1])])

    G_matrix.deleteVertex(vertexes[names.index('K')])
    G_matrix.deleteEdge(vertexes[names.index('E')], vertexes[names.index('W')])
    G_matrix.deleteEdge(vertexes[names.index('W')], vertexes[names.index('E')])
    polska.draw_map(G_matrix.edges())


test_list()
test_matrix()