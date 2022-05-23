from math import inf


class Vertex:
    def __init__(self, key, data=None):
        self.vertex = (key, data)

    def __eq__(self, other):
        if type(self) is type(other):
            return (self.vertex[0], self.vertex[1]) == (other[0], other[1])

        else:
            return False

    def __hash__(self):
        return hash(self.vertex[0])

    def __repr__(self):
        return repr(self.vertex)

    def __getitem__(self, item):
        return self.vertex[item]


class Edge:
    def __init__(self, vertex_1_key, vertex_2_key, weight=0):
        self.edge = (vertex_1_key, vertex_2_key)
        self.weight = weight

    def __repr__(self):
        return repr(self.edge)

    def __getitem__(self, item):
        return self.edge[item]


class AdjacencyList:
    def __init__(self):
        self.vertices = []
        self.list = {}

    # dodawanie
    def insert_vertex(self, vertex):
        self.vertices.append(vertex)
        index = self.get_vertex_id(vertex[0])

        self.list[index] = []

    def insert_edge(self, edge):
        i = self.get_vertex_id(edge[0])
        j = self.get_vertex_id(edge[1])

        self.list[i] = self.list[i] + [(j, edge.weight)]
        self.list[j] = self.list[j] + [(i, edge.weight)]

    # usuwanie
    def delete_vertex(self, vertex_key):
        index = self.get_vertex_id(vertex_key)
        self.vertices.pop(index)

        list = {}
        for key, value in self.list.items():
            if key < index:
                adjacency = []
                for element in value:
                    if element < index:
                        adjacency.append(element)

                    elif element > index:
                        adjacency.append(element - 1)

                    list[key] = adjacency

            elif key > index:
                adjacency = []
                for element in value:
                    if element < index:
                        adjacency.append(element)

                    elif element > index:
                        adjacency.append(element - 1)

                    list[key - 1] = adjacency

        self.list = list

    def delete_edge(self, vertex_1_key, vertex_2_key):
        i = self.get_vertex_id(vertex_1_key)
        j = self.get_vertex_id(vertex_2_key)

        # krawedzie były dodawane podwójnie
        self.list[i].remove(j)
        self.list[j].remove(i)

    # odczyt
    def get_vertex_id(self, vertex_key):
        for index, vertex in enumerate(self.vertices):
            if vertex[0] == vertex_key:
                return index

        else:
            return None

    def get_vertex(self, index):
        vertex = self.vertices[index]

        return vertex

    def neighbours(self, vertex_key):
        neighbours_list = []
        vertex_index = self.get_vertex_id(vertex_key)

        for element in self.list[vertex_index]:
            neighbour_key = self.get_vertex(element[0])[0]
            neighbours_list.append((neighbour_key, element[1]))

        return neighbours_list

    # odczyt własności grafu
    def order(self):
        return len(self.vertices)

    def size(self):
        edges = self.edges()

        return len(edges)

    def edges(self):
        edges = []

        for index, value in self.list.items():
            for element in value:
                edges.append((self.get_vertex(index)[0], self.get_vertex(element[0])[0], element[1]))

        return edges

    def __str__(self):
        strings = []

        for item in self.list.items():
            strings.append(str(item))

        return '\n'.join(strings)

    def mst(self):
        # struktura drzewa MST
        tree = AdjacencyList()

        for index in self.list.items():
            tree.insert_vertex(self.get_vertex(index[0])[0])

        sum_weight = 0

        # listy
        n = self.order()

        parent = [0 for v in range(n)]
        distance = [inf for v in range(n)]
        not_in_tree = [v for v in range(n)]

        # wierzchotek startowy
        start = 0

        distance[start] = 0
        not_in_tree.remove(start)
        last_vertex = start

        while not_in_tree:
            for i in not_in_tree:
                neighbours = self.neighbours(self.get_vertex(last_vertex)[0])
                for j in neighbours:
                    if j[1] < distance[self.get_vertex_id(j[0])]:
                        parent[self.get_vertex_id(j[0])] = last_vertex
                        distance[self.get_vertex_id(j[0])] = j[1]

            minimum = inf
            for v in not_in_tree:
                if distance[v] < minimum:
                    minimum = distance[v]
                    last_vertex = v

            not_in_tree.remove(last_vertex)

            neighbours = self.neighbours(self.get_vertex(last_vertex)[0])
            second_vertex = [v for v in neighbours if v[0] == self.get_vertex(parent[last_vertex])[0]]
            weight = second_vertex[0][1]

            edge = Edge(self.get_vertex(parent[last_vertex])[0], self.get_vertex(last_vertex)[0], weight)
            tree.insert_edge(edge)

            sum_weight += weight

        return tree, sum_weight


def print_graph(graph):
    n = graph.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = graph.get_vertex(i)
        print(v[0], end=" -> ")
        nbrs = graph.neighbours(v[0])
        for (j, w) in nbrs:
            print(j, w, end="; ")
        print()
    print("-------------------")


def mst_graph():
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]

    graph = AdjacencyList()

    for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        vertex = Vertex(key)

        graph.insert_vertex(vertex)

    for element in graf:
        edge = Edge(element[0], element[1], element[2])
        graph.insert_edge(edge)

    tree, suma = graph.mst()

    print_graph(tree)


def main():
    mst_graph()


main()
