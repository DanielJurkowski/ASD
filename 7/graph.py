import polska


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
    def __init__(self, vertex_1_key, vertex_2_key):
        self.edge = (vertex_1_key, vertex_2_key)

    def __repr__(self):
        return repr(self.edge)

    def __getitem__(self, item):
        return self.edge[item]


# macierz sąsiedztwa
class AdjacencyMatrix:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    # dodawanie
    def insert_vertex(self, vertex):
        self.vertices.append(vertex)

        index = self.get_vertex_id(vertex[0])

        matrix = []
        for row in self.matrix:
            row.insert(index, 0)
            matrix.append(row)

        matrix.append([0] * (len(self.matrix) + 1))
        self.matrix = matrix

    def insert_edge(self, edge):
        i = self.get_vertex_id(edge[0])
        j = self.get_vertex_id(edge[1])

        self.matrix[i][j] += 1

    # usuwanie
    def delete_vertex(self, vertex_key):
        index = self.get_vertex_id(vertex_key)
        self.vertices.pop(index)

        matrix = []
        for i, row in enumerate(self.matrix):
            if i != index:
                row = row[:index] + row[index + 1:]
                matrix.append(row)

        self.matrix = matrix

    def delete_edge(self, vertex_1_key, vertex_2_key):
        i = self.get_vertex_id(vertex_1_key)
        j = self.get_vertex_id(vertex_2_key)

        # krawedzie były dodawane podwójnie
        if self.matrix[i][j] > 0:
            self.matrix[i][j] -= 1

        if self.matrix[j][i] > 0:
            self.matrix[j][i] -= 1

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

        for index, element in enumerate(self.matrix[vertex_index]):
            if element >= 1:
                neighbour_key = self.get_vertex(index)[0]
                neighbours_list.append(neighbour_key)

            else:
                pass

        return neighbours_list

    # odczyt własności grafu
    def order(self):
        return len(self.vertices)

    def size(self):
        edges = self.edges()

        return len(edges)

    def edges(self):
        edges = []

        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element >= 1:
                    edges.append((self.get_vertex(i)[0], self.get_vertex(j)[0]))

        return edges

    def __str__(self):
        strings = []

        for row in self.matrix:
            strings.append(str(row))

        return '\n'.join(strings)


# lista sąsiedztwa
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

        self.list[i] = self.list[i] + [j]

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

        for index in self.list[vertex_index]:
            neighbour_key = self.get_vertex(index)[0]
            neighbours_list.append(neighbour_key)

        return neighbours_list

    # odczyt własności grafu
    def order(self):
        return len(self.vertices)

    def size(self):
        edges = self.edges()

        return len(edges)

    def edges(self):
        edges = []

        for key, value in self.list.items():
            for element in value:
                if element >= 1:
                    edges.append((self.get_vertex(key)[0], self.get_vertex(element)[0]))

        return edges

    def __str__(self):
        strings = []

        for item in self.list.items():
            strings.append(str(item))

        return '\n'.join(strings)


colors = ['red', 'green', 'blue', 'white', 'yellow', 'purple', 'orange', 'brown']


def dfs(graph, start_vertex):
    coloured = {vertex: colors[0] for vertex in graph.keys()}


def adjacency_matrix():
    graph = AdjacencyMatrix()

    for voivodeship in polska.polska:
        (x, y, key) = voivodeship
        vertex = Vertex(key, (x, y))

        graph.insert_vertex(vertex)

    for element in polska.graf:
        edge = Edge(element[0], element[1])
        graph.insert_edge(edge)

    graph.delete_vertex('K')
    graph.delete_edge('W', 'E')

    print(graph)
    polska.draw_map(graph.edges())


def adjacency_list():
    graph = AdjacencyList()

    for voivodeship in polska.polska:
        (x, y, key) = voivodeship
        vertex = Vertex(key, (x, y))

        graph.insert_vertex(vertex)

    for element in polska.graf:
        edge = Edge(element[0], element[1])
        graph.insert_edge(edge)

    graph.delete_vertex('K')
    graph.delete_edge('W', 'E')

    print(graph)
    polska.draw_map(graph.edges())


def main():
    choice = input('matrix or list: ')

    if choice == 'matrix':
        adjacency_matrix()

    if choice == 'list':
        adjacency_list()

    else:
        main()


main()
