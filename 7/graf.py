import polska
from typing import List, Tuple, Dict

id_ = str
idx = int
data_ = str
Vertex = Tuple[id_, data_]

#COLORS = [turtle.color((r * 85, g * 85, b * 85)) for r in range(1, 4) for g in range(1, 4) for b in range(1, 4)]
COLORS = ['white', 'red', 'blue', 'yellow', 'green', 'purple', 'cyan', 'magenta']


class Adjmat:
    def __init__(self):
        self.data: List[Vertex] = []
        self.matrix: List[List[int]] = []

    def map(self, vertex_id) -> idx:
        for i, data in enumerate(self.data):
            if data[0] == vertex_id:
                return i
        else:
            raise ValueError

    def demap(self, id_) -> Vertex:
        return self.data[id_]

    def insertVertex(self, data, vertex_id):
        self.data.append((vertex_id, data))
        i = self.map(vertex_id)
        new_matrix = []
        for row in self.matrix:
            row.insert(i, 0)
            new_matrix.append(row)
        new_matrix.append([0] * (len(self.matrix) + 1))
        self.matrix = new_matrix

    def insertEdge(self, vertex1_id, vertex2_id):
        i = self.map(vertex1_id)
        j = self.map(vertex2_id)
        self.matrix[i][j] = 1

    def deleteVertex(self, vertex_id):
        i = self.map(vertex_id)
        self.data.remove(self.demap(i))
        new_matrix = []
        for j, row in enumerate(self.matrix):
            if i == j:
                continue
            row = row[:i] + row[i + 1:]
            new_matrix.append(row)
        self.matrix = new_matrix

    def deleteEdge(self, vertex1_id, vertex2_id):
        i = self.map(vertex1_id)
        j = self.map(vertex2_id)
        self.matrix[i][j] = 0
        self.matrix[j][i] = 0

    def getVertex(self, vertex_id):
        return self.data[self.map(vertex_id)]

    def neighbors(self, vertex_id):
        return [self.demap(i)[0] for i, elem in enumerate(self.matrix[self.map(vertex_id)]) if elem == 1]

    def order(self):
        return len(self.matrix)

    def size(self):
        return sum([sum(row) for row in self.matrix]) // 2

    def edges(self):
        return [(self.demap(i)[0], self.demap(j)[0]) for i, row in enumerate(self.matrix)
                for j, elem in enumerate(row) if elem == 1]

    def coloring(self, traversal: str):
        if traversal.lower() == 'bfs':
            lst = adjmat_to_adjlist_(self.matrix)
            return [(self.demap(p)[0], c) for (p, c) in bfs(lst, 0)]
        elif traversal.lower() == 'dfs':
            lst = adjmat_to_adjlist_(self.matrix)
            return [(self.demap(p)[0], c) for (p, c) in dfs(lst, 0)]
        else:
            raise NotImplemented

    def __str__(self):
        strings = []

        for row in self.matrix:
            strings.append(str(row))

        return '\n'.join(strings)


class Adjlist:
    def __init__(self):
        self.data: List[Vertex] = []
        self.list: Dict[idx: List[idx]] = {}

    def map(self, vertex_id) -> idx:
        for i, data in enumerate(self.data):
            if data[0] == vertex_id:
                return i
        else:
            raise ValueError

    def demap(self, id_) -> Vertex:
        return self.data[id_]

    def insertVertex(self, data, vertex_id):
        self.data.append((vertex_id, data))
        i = self.map(vertex_id)
        self.list[i] = []

    def insertEdge(self, vertex1_id, vertex2_id):
        i = self.map(vertex1_id)
        j = self.map(vertex2_id)
        ni = self.list[i]
        self.list[i] = ni + [j]

    def deleteVertex(self, vertex_id):
        i = self.map(vertex_id)
        self.data.remove(self.demap(i))
        new_list = {}
        for k, v in self.list.items():
            if k < i:
                lst = []
                for n in v:
                    if n < i:
                        lst.append(n)
                    elif n > i:
                        lst.append(n-1)
                new_list[k] = lst
            elif k > i:
                lst = []
                for n in v:
                    if n < i:
                        lst.append(n)
                    elif n > i:
                        lst.append(n-1)
                new_list[k-1] = lst
        self.list = new_list

    def deleteEdge(self, vertex1_id, vertex2_id):
        i = self.map(vertex1_id)
        j = self.map(vertex2_id)
        ni = self.list[i]
        ni.remove(j)
        nj = self.list[j]
        nj.remove(i)
        self.list[i] = ni
        self.list[j] = nj

    def getVertex(self, vertex_id):
        return self.data[self.map(vertex_id)]

    def neighbors(self, vertex_id):
        return [self.demap(k)[0] for k in self.list[self.map(vertex_id)]]

    def order(self):
        return len(self.list.keys())

    def size(self):
        return sum([len(row) for row in self.list.values()]) // 2

    def edges(self):
        e = []
        for k, v in self.list.items():
            for n in v:
                e.append((self.demap(k)[0], self.demap(n)[0]))
        return e

    def coloring(self, traversal: str):
        if traversal.lower() == 'bfs':
            return [(self.demap(p)[0], c) for (p, c) in bfs(self.list, 4)]
        elif traversal.lower() == 'dfs':
            return [(self.demap(p)[0], c) for (p, c)in dfs(self.list, 0)]
        else:
            raise NotImplemented


def adjmat_to_adjlist_(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    return {i: [j for j, e in enumerate(row) for _ in range(e)]
            for i, row in enumerate(adjmat) if row != len(adjmat) * [0]}


def dfs(G: Dict[int, List[int]], s: int) -> List[Tuple[int, Tuple[int, int, int]]]:
    last_used_color_id = 0
    stos = [s]
    coloured: Dict[int, Tuple[int, int, int]] = {v: COLORS[0] for v in G.keys()}
    visited = []
    while stos:
        v = stos.pop()
        if v not in visited:
            visited.append(v)
            i = 1
            while coloured[v] in map(lambda x: coloured[x], G[v]):
                coloured[v] = COLORS[i]
                if i > last_used_color_id:
                    last_used_color_id = i
                i += 1
            stos += G[v][::-1]
    return [(k, v) if v != COLORS[0] else (k, COLORS[last_used_color_id]) for k, v in coloured.items()]


def bfs(G: Dict[int, List[int]], s: int) -> List[Tuple[int, Tuple[int, int, int]]]:
    last_used_color_id = 0
    visited = [s]
    coloured: Dict[int, Tuple[int, int, int]] = {v: COLORS[0] for v in G.keys()}
    queue = [s]
    while queue:
        n = queue.pop(0)
        for neighbour in G[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                i = 1
                while coloured[neighbour] in map(lambda x: coloured[x], G[neighbour]):
                    coloured[neighbour] = COLORS[i]
                    if i > last_used_color_id:
                        last_used_color_id = i
                    i += 1
                queue.append(neighbour)
    return [(k, v) if v != COLORS[0] else (k, COLORS[last_used_color_id]) for k, v in coloured.items()]


def test_adjmat():
    graph = Adjmat()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x, y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)
    print(graph.neighbors('K'))
    print(graph.size())
    print(graph.order())
    graph.deleteVertex("K")
    graph.deleteEdge('W', 'E')
    polska.draw_map(graph.edges())


def test_adjlist():
    graph = Adjlist()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x,y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)

    print(graph.neighbors('K'))
    graph.deleteVertex("K")
    graph.deleteEdge('W', 'E')
    polska.draw_map(graph.edges())


def test_adjmat_coloring_dfs():
    graph = Adjmat()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x, y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)

    polska.draw_map(graph.edges(), graph.coloring(traversal='dfs'))


def test_adjlist_coloring_dfs():
    graph = Adjlist()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x,y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)

    polska.draw_map(graph.edges(), graph.coloring(traversal='dfs'))

def test_adjmat_coloring_bfs():
    graph = Adjmat()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x, y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)

    polska.draw_map(graph.edges(), graph.coloring(traversal='bfs'))


def test_adjlist_coloring_bfs():
    graph = Adjlist()

    for woj in polska.polska:
        (x, y, idx) = woj
        graph.insertVertex((x,y), idx)

    for pol in polska.graf:
        graph.insertEdge(*pol)

    polska.draw_map(graph.edges(), graph.coloring(traversal='bfs'))


print('[1] Test grafu reprezentowanego za pomocą macierzy sąsiedztwa')
print('[2] Test grafu reprezentowanego za pomocą listy sąsiedztwa')
print('[3] Test kolorowania grafu reprezentowanego za pomocą macierzy sąsiedztwa przy pomocy dfs')
print('[4] Test kolorowania grafu reprezentowanego za pomocą listy sąsiedztwa przy pomocy dfs')
print('[5] Test kolorowania grafu reprezentowanego za pomocą macierzy sąsiedztwa przy pomocy bfs')
print('[6] Test kolorowania grafu reprezentowanego za pomocą listy sąsiedztwa przy pomocy bfs')
ans = input('Co chciałaby Szanowna Pani Doktor sprawdzić? ')
if ans == '1':
    test_adjmat()
if ans == '2':
    test_adjlist()
if ans == '3':
    test_adjmat_coloring_dfs()
if ans == '4':
    test_adjlist_coloring_dfs()
if ans == '5':
    test_adjmat_coloring_bfs()
if ans == '6':
    test_adjlist_coloring_bfs()
