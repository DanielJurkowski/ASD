import numpy as np
from copy import deepcopy


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


class Edge:
    def __init__(self, weight=None):
        self.weight = weight

    def __str__(self):
        string = f'{self.weight}'

        return string

    def __repr__(self):
        return repr(self.weight)


# macierz sąsiedztwa
class AdjacencyMatrix:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    # dodawanie
    def insert_vertex(self, vertex):
        self.vertices.append(vertex)

        index = self.get_vertex_id(vertex.key)

        matrix = []
        for row in self.matrix:
            row.insert(index, 0)
            matrix.append(row)

        matrix.append([0] * (len(self.matrix) + 1))
        self.matrix = matrix

    def insert_edge(self, vertex_1, vertex_2, edge):
        if vertex_1 not in self.vertices:
            self.insert_vertex(vertex_1)

        if vertex_2 not in self.vertices:
            self.insert_vertex(vertex_2)

        i = self.get_vertex_id(vertex_1.key)
        j = self.get_vertex_id(vertex_2.key)

        self.matrix[i][j] += 1
        self.matrix[j][i] += 1

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

        if self.matrix[i][j] > 0:
            self.matrix[i][j] -= 1

        if self.matrix[j][i] > 0:
            self.matrix[j][i] -= 1

    # odczyt
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
        neighbours_list = []
        vertex_index = self.get_vertex_id(vertex_key)

        for index, element in enumerate(self.matrix[vertex_index]):
            if element >= 1:
                neighbour = self.get_vertex(index)
                neighbours_list.append(neighbour.key)

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
                    edges.append((self.get_vertex(i).key, self.get_vertex(j).key))

        return edges

    def __str__(self):
        strings = []

        for row in self.matrix:
            strings.append(str(row))

        return '\n'.join(strings)


def matrix(graph_1, graph_2):
    matrix = np.zeros((graph_1.order(), graph_2.order()))
    matrix_1 = np.array(graph_1.matrix)
    matrix_2 = np.array(graph_2.matrix)

    for row in range(len(matrix)):
        g1_vertex_deg = sum(matrix_1[:, row])
        for column in range(len(matrix[0])):
            g2_vertex_deg = sum(matrix_2[:, column])

            if g2_vertex_deg >= g1_vertex_deg:
                matrix[row, column] = 1

    return matrix


def prune(matrix, graph_1, graph_2):
    graph_1_matrix = np.array(graph_1.matrix)
    graph_2_matrix = np.array(graph_2.matrix)

    row, column = matrix.shape
    for row in range(row):
        for column in range(column):
            if matrix[row, column] == 1:
                stop = False

                for i in graph_1_matrix[row]:
                    for j in graph_2_matrix[column]:
                        if matrix[i, j] == 1:
                            stop = True
                            break

                        if stop:
                            break

                else:
                    matrix[row, column] = 0


def ullman_1(used_columns, current_row, graph_1, graph_2):
    matrix = np.zeros((graph_1.order(), graph_2.order()))

    if current_row == matrix.shape[0]:
        matrix_copy = matrix.copy


    matrix_copy = matrix.copy


def main():
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    graf_P = AdjacencyMatrix()
    for edge in graph_P:
        graf_P.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))

    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]

    graf_G = AdjacencyMatrix()
    for edge in graph_G:
        graf_G.insert_edge(Vertex(edge[0]), Vertex(edge[1]), Edge(edge[2]))

    print(matrix(graf_P, graf_G))


main()
