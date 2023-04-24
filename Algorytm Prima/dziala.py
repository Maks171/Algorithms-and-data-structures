# skończone
import graf_mst


class Vertex:
    def __init__(self, key, colour=0):
        self.key = key
        self.colour = colour

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, weight):
        self.weight = weight


class Graph:
    def __init__(self, *args, **kwargs):
        self.lst = []
        self.dct = {}
        self.tab = []

    def get_vertex_idx(self, vertex):
        if vertex in self.dct.keys():
            return self.dct[vertex]
        else:
            return None

    def get_vertex(self, vertex_idx):
        if vertex_idx < len(self.lst):
            return self.lst[vertex_idx]
        else:
            return None

    def order(self):
        return len(self.lst)


class ListGraph(Graph):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def insert_vertex(self, vertex):
        self.lst.append(vertex)
        self.dct[vertex] = self.lst.index(vertex)
        self.tab.append([])

    def insert_edge(self, vertex1, vertex2, edge):
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        self.tab[idx1].append((idx2, edge.weight))

    def delete_vertex(self, vertex):
        idx = self.get_vertex_idx(vertex)
        self.tab.pop(idx)
        for i in self.tab:
            idx_to_remove = -1
            for j in range(len(i)):
                if i[j][0] == idx:
                    idx_to_remove = j
                if i[j][0] > idx:
                    i[j] = i[j][0] - 1, i[j][1]
            if idx_to_remove != -1:
                i.pop(idx_to_remove)
        self.lst.remove(vertex)
        self.dct.pop(vertex)
        for i in range(len(self.lst)):
            self.dct[self.lst[i]] = i

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_idx(vertex1)
        idx2 = self.get_vertex_idx(vertex2)
        weight = -1
        for i in self.tab[idx1]:
            if i[0] == idx2:
                weight = i[1]
        if weight != -1:
            self.tab[idx1].remove((idx2, weight))
            self.tab[idx2].remove((idx1, weight))

    def neighbours(self, vertex_idx):
        return self.tab[vertex_idx]

    def size(self):
        count = 0
        for i in self.tab:
            count += len(i)

        return count/2

    def edges(self):
        edges_lst = []
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                edges_lst.append((self.get_vertex(i).key, self.get_vertex(self.tab[i][j][0]).key))
        return edges_lst


def prim_mst(graph):
    size = graph.order()
    intree = [0] * size
    distance = [float('inf')] * size
    parent = [-1] * size
    mst_tree = ListGraph()
    for i in graph.dct.keys():
        mst_tree.insert_vertex(Vertex(i.key))

    vertex_idx = 0
    while intree[vertex_idx] == 0:
        intree[vertex_idx] = 1
        neighbours = graph.neighbours(vertex_idx)
        for i in neighbours:
            if intree[i[0]] == 0 and i[1] < distance[i[0]]:
                distance[i[0]] = i[1]
                parent[i[0]] = vertex_idx

        min_distance = float('inf')
        idx = -1
        for i in range(size):
            if intree[i] == 0 and distance[i] < min_distance:
                min_distance = distance[i]
                idx = i
        if idx != -1:
            mst_tree.insert_edge(mst_tree.get_vertex(idx), mst_tree.get_vertex(parent[idx]), Edge(min_distance))
            mst_tree.insert_edge(mst_tree.get_vertex(parent[idx]), mst_tree.get_vertex(idx), Edge(min_distance))
            vertex_idx = idx

    return mst_tree


def print_graph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.get_vertex(i)
        print(v.key, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.get_vertex(j).key, w, end=";")
        print()
    print("-------------------")


if __name__ == "__main__":
    gr = ListGraph()
    for k in graf_mst.graf:
        if Vertex(k[0]) not in gr.dct.keys():
            gr.insert_vertex(Vertex(k[0]))
        if Vertex(k[1]) not in gr.dct.keys():
            gr.insert_vertex(Vertex(k[1]))
        gr.insert_edge(Vertex(k[0]), Vertex(k[1]), Edge(k[2]))
        gr.insert_edge(Vertex(k[1]), Vertex(k[0]), Edge(k[2]))

    mst = prim_mst(gr)

    print_graph(mst)
