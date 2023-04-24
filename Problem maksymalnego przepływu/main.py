import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, weight=1):
        self.weight = weight


class Graph:
    def __init__(self):
        self.lst = []
        self.dct = {}
        self.tab = []

    def insertVertex(self, vertex):
        self.lst.append(vertex)
        self.dct[vertex] = self.lst.index(vertex)
        if len(self.tab) == 0:
            self.tab.append([0])
        else:
            for i in range(len(self.tab)):
                self.tab[i].append(0)
            self.tab.append([0] * len(self.tab[0]))

    def insertEdge(self, vertex1, vertex2, edge=Edge()):
        self.tab[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = \
            self.tab[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = edge.weight

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        self.tab.pop(idx)
        for i in range(len(self.tab)):
            self.tab[i].pop(idx)
        self.lst.remove(vertex)
        self.dct.pop(vertex)
        for i in range(len(self.lst)):
            self.dct[i] = i

    def deleteEdge(self, vertex1, vertex2):
        self.tab[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = \
            self.tab[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = None

    def getVertexIdx(self, vertex):
        if vertex in self.dct.keys():
            return self.dct[vertex]
        return None

    def getVertex(self, vertex_idx):
        if vertex_idx < len(self.lst):
            return self.lst[vertex_idx]
        return None

    def neighbours(self, vertex_idx):
        neighbours_lst = []
        for i in range(len(self.tab[vertex_idx])):
            if self.tab[vertex_idx][i] is not None:
                neighbours_lst.append(i)
        return neighbours_lst

    def order(self):
        return len(self.lst)

    def size(self):
        count = 0
        for i in range(len(self.tab)):
            for j in range(i + 1, len(self.tab[0])):
                if self.tab[i][j] is not None:
                    count += 1
        return count

    def edges(self):
        result = []
        for i in range(len(self.tab)):
            for j in range(len(self.tab[0])):
                if self.tab[i][j] is not None:
                    result.append((self.getVertex(i).key, self.getVertex(j).key))
        return result


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v.key, end=" -> ")
        nbrs = g.neighbours(i)
        for j in nbrs:
            print(g.getVertex(j).key, 1, end=";")
        print()
    print("-------------------")


def ullman(G, P, M=None, current_row=0, used_columns=None, list_matrixes=None, no_recursion=0, M0_flag=False, M0=None,
           prune_flag=False):
    if M is None:
        M = np.ones((P.shape[1], G.shape[0]))
    no_recursion += 1
    if list_matrixes is None:
        used_columns = M.shape[1] * [0]
        list_matrixes = []

    if M0_flag is True:
        M0 = np.zeros(M.shape)
        for k in range(len(P)):
            count_p = 0
            for i in P[k]:
                if i == 1:
                    count_p += 1
            for i in range(len(G)):
                count_g = 0
                for j in G[i]:
                    if j == 1:
                        count_g += 1
                if count_g >= count_p:
                    M0[k, i] = 1

    if M0 is None:
        M0 = np.ones(M.shape)

    if current_row == M.shape[0]:
        if (P == (M @ (M @ G).T)).all():
            list_matrixes.append(M.copy())
        return list_matrixes, no_recursion

    M_prim = M.copy()

    if prune_flag is True:
        changed = True
        while changed:
            changed = False
            for i in range(len(M_prim)):
                for j in range(len(M_prim[i])):
                    if M_prim[i][j]:
                        P_neighbours = P[i]
                        G_neighbours = G[j]
                        for x in range(len(P_neighbours)):
                            if P_neighbours[x]:
                                is_mapped = False
                                for y in range(len(G_neighbours)):
                                    if G_neighbours[y]:
                                        if M_prim[x, y]:
                                            is_mapped = True
                                            break
                                if is_mapped is False:
                                    M_prim[i, j] = 0
                                    changed = True
                                    break
        if not True in M_prim[0] or not True in M_prim[1] or not True in M_prim[2]:
            return list_matrixes, no_recursion

    for c in range(len(used_columns)):
        if used_columns[c] == 0 and M0[current_row, c]:
            M_prim[current_row, :] = 0
            M_prim[current_row, c] = 1
            used_columns[c] = 1
            list_matrixes, no_recursion = ullman(G, P, M_prim, current_row + 1, used_columns, list_matrixes,
                                                 no_recursion, False, M0, prune_flag)
            used_columns[c] = 0

    return list_matrixes, no_recursion


graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

G = Graph()
P = Graph()

for i in graph_G:
    if Vertex(i[0]) not in G.dct.keys():
        G.insertVertex(Vertex(i[0]))
    if Vertex(i[1]) not in G.dct.keys():
        G.insertVertex(Vertex(i[1]))
    G.insertEdge(Vertex(i[0]), Vertex(i[1]))
    G.insertEdge(Vertex(i[1]), Vertex(i[0]))

for i in graph_P:
    if Vertex(i[0]) not in P.dct.keys():
        P.insertVertex(Vertex(i[0]))
    if Vertex(i[1]) not in P.dct.keys():
        P.insertVertex(Vertex(i[1]))
    P.insertEdge(Vertex(i[0]), Vertex(i[1]))
    P.insertEdge(Vertex(i[1]), Vertex(i[0]))

G = np.array(G.tab)
P = np.array(P.tab)

M_lst, n = ullman(G, P)
print(len(M_lst), n)

M_lst, n = ullman(G, P, M0_flag=True)
print(len(M_lst), n)

M_lst, n = ullman(G, P, M0_flag=True, prune_flag=True)
print(len(M_lst), n)
