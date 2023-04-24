import numpy as np


class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self):
        pass


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
        self.adjacency_matrix[self.dictionary[vertex2]][self.dictionary[vertex1]] = 1

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

def ullman(used_columns, current_row, G, P, M):
    pass


graph_G = AdjacencyMatrix()
graph_G.insertVertex('A')
graph_G.insertVertex('B')
graph_G.insertVertex('C')
graph_G.insertVertex('D')
graph_G.insertVertex('E')
graph_G.insertVertex('F')
graph_G.insertEdge('A', 'B')
graph_G.insertEdge('B', 'F')
graph_G.insertEdge('B', 'C')
graph_G.insertEdge('C', 'D')
graph_G.insertEdge('C', 'E')
graph_G.insertEdge('D', 'E')
G = np.array(graph_G.adjacency_matrix)
print(G)

graph_P = AdjacencyMatrix()
graph_P.insertVertex('A')
graph_P.insertVertex('B')
graph_P.insertVertex('C')
graph_P.insertEdge('A', 'B')
graph_P.insertEdge('B', 'C')
graph_P.insertEdge('A', 'C')
P = np.array(graph_P.adjacency_matrix)
print(P)

