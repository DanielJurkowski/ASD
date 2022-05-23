from math import inf


class Edge:
    def __init__(self, capacity=None, isResidual=False):
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity
        self.isResidual = isResidual

    def __str__(self):
        string = f'{self.capacity} {self.flow} {self.residual} {self.isResidual}'

        return string

    def __repr__(self):
        return repr((self.capacity, self.flow, self.residual, self.isResidual))


class Vertex:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __eq__(self, other):
        if type(self) is type(other):
            return (self.key, self.data) == (other.key, other.data)

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        string = f'{self.key} {self.data}'

        return string

    def __repr__(self):
        return repr((self.key, self.data))


class AdjacencyList:
    def __init__(self):
        self.vertices = []
        self.list = {}

    def insert_vertex(self, vertex):
        self.vertices.append(vertex)
        index = self.get_vertex_id(vertex.key)

        self.list[index] = []

    def insert_edge(self, vertex_1, vertex_2, edge):
        if vertex_1 not in self.vertices:
            self.insert_vertex(vertex_1)

        if vertex_2 not in self.vertices:
            self.insert_vertex(vertex_2)

        i = self.get_vertex_id(vertex_1.key)
        j = self.get_vertex_id(vertex_2.key)

        self.list[i] = self.list[i] + [[j, edge]]

    def delete_vertex(self, vertex_key):
        index = self.get_vertex_id(vertex_key)
        self.vertices.pop(index)

        list = {}
        for key, value in self.list.items():
            if key < index:
                adjacency = []

                if len(value) == 0:
                    list[key] = adjacency

                for element in value:
                    if element[0] < index:
                        adjacency.append([element[0], element[1]])

                    elif element[0] > index:
                        adjacency.append([element[0] - 1, element[1]])

                    list[key] = adjacency

            elif key > index:
                adjacency = []

                if len(value) == 0:
                    list[key - 1] = adjacency

                for element in value:
                    if element[0] < index:
                        adjacency.append([element[0], element[1]])

                    elif element[0] > index:
                        adjacency.append([element[0] - 1, element[1]])

                    list[key - 1] = adjacency

        self.list = list

    def delete_edge(self, vertex_1_key, vertex_2_key):
        i = self.get_vertex_id(vertex_1_key)
        j = self.get_vertex_id(vertex_2_key)

        for index, vertex in enumerate(self.list[i]):
            if self.list[i][index][0] == j:
                self.list[i].pop(index)

    def get_vertex_id(self, vertex_key):
        for v in self.vertices:
            if vertex_key == v.key:
                return self.vertices.index(v)

        else:
            return None

    def get_vertex(self, index):
        vertex = self.vertices[index]

        return vertex

    def neighbours(self, vertex_key):
        vertex_index = self.get_vertex_id(vertex_key)
        neighbours_list = self.list[vertex_index]

        return neighbours_list

    def order(self):
        return len(self.vertices)

    def size(self):
        edges = self.edges()

        return len(edges)

    def edges(self):
        edges = []

        for index, value in self.list.items():
            for element in value:
                edges.append((index, element[0], element[1]))

        return edges

    def bfs(self, start_key):
        visited = [False] * self.order()
        parent = [None] * self.order()
        queue = []

        start_index = self.get_vertex_id(start_key)
        queue.append(start_key)
        visited[start_index] = True

        while queue:
            vertex = queue.pop(0)
            neighbours = self.neighbours(vertex)

            for neighbour in neighbours:
                index = neighbour[0]
                if visited[index] is False and neighbour[1].residual > 0:
                    queue.append(self.get_vertex(index).key)
                    visited[index] = True
                    parent[index] = self.get_vertex_id(vertex)

        return parent

    def analyse_path(self, start_key, end_key):
        parent = self.bfs(start_key)
        start_index = self.get_vertex_id(start_key)
        end_index = self.get_vertex_id(end_key)
        minimal_capacity = inf

        if parent[end_index] is None:
            minimal_capacity = 0

            return minimal_capacity

        else:
            index = end_index
            while index != start_index:
                parent_index = parent[index]
                neighbours = self.neighbours(self.get_vertex(parent_index).key)

                edge = None
                for neighbour in neighbours:
                    if neighbour[0] == index and neighbour[1].isResidual is False:
                        edge = neighbour[1]
                        break

                if edge.residual < minimal_capacity:
                    minimal_capacity = edge.residual

                index = parent_index

        return minimal_capacity

    def path_augumentation(self, start_key, end_key):
        parent = self.bfs(start_key)
        minimal_capacity = self.analyse_path(start_key, end_key)
        start_index = self.get_vertex_id(start_key)
        end_index = self.get_vertex_id(end_key)

        index = end_index
        while index != start_index:
            parent_index = parent[index]

            neighbours_parent = self.neighbours(self.get_vertex(parent_index).key)
            for neighbour in neighbours_parent:
                if neighbour[0] == index and neighbour[1].isResidual is False:
                    neighbour[1].flow += minimal_capacity
                    neighbour[1].residual -= minimal_capacity

            neighbours_index = self.neighbours(self.get_vertex(index).key)
            for neighbour in neighbours_index:
                if neighbour[0] == parent_index and neighbour[1].isResidual is True:
                    neighbour[1].residual += minimal_capacity

            index = parent_index

    def fk(self, start_key, end_key):
        parent = self.bfs(start_key)
        minimal_capacity = self.analyse_path(start_key, end_key)
        start_index = self.get_vertex_id(start_key)
        end_index = self.get_vertex_id(end_key)
        sum_flow = 0

        index = end_index
        while index != start_index:
            if parent[index] is None:
                return "Error"

            index = parent[index]

        while minimal_capacity > 0:
            sum_flow += minimal_capacity
            self.path_augumentation(start_key, end_key)
            minimal_capacity = self.analyse_path(start_key, end_key)

        return sum_flow

    def __str__(self):
        strings = []

        for item in self.list.items():
            strings.append(str(item))

        return '\n'.join(strings)


def print_graph(graph):
    n = graph.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = graph.get_vertex(i)
        print(v.key, end=" -> ")
        nbrs = graph.neighbours(v.key)
        for neigh in nbrs:
            print(graph.get_vertex(neigh[0]).key, neigh[1].capacity,
                  neigh[1].flow, neigh[1].residual, neigh[1].isResidual, end="; ")
        print()
    print("-------------------")


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    # graf 1
    graf0 = AdjacencyList()

    for edge in graf_0:
        graf0.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))
        graf0.insert_edge(Vertex(edge[1]), Vertex(edge[0]), Edge(0, True))

    print(graf0.fk('s', 't'))
    print_graph(graf0)

    # graf 2
    graf1 = AdjacencyList()

    for edge in graf_1:
        graf1.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))
        graf1.insert_edge(Vertex(edge[1]), Vertex(edge[0]), Edge(0, True))

    print(graf1.fk('s', 't'))
    print_graph(graf1)

    # graf 3
    graf2 = AdjacencyList()

    for edge in graf_2:
        graf2.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))
        graf2.insert_edge(Vertex(edge[1]), Vertex(edge[0]), Edge(0, True))

    print(graf2.fk('s', 't'))
    print_graph(graf2)

    # graf 4
    graf3 = AdjacencyList()

    for edge in graf_3:
        graf3.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))
        graf3.insert_edge(Vertex(edge[1]), Vertex(edge[0]), Edge(0, True))

    print(graf3.fk('s', 't'))
    print_graph(graf3)


main()
