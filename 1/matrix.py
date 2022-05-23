# NIESKOŃCZONE

def matrix_string(matrix):
    strings = []

    for row in matrix:
        strings.append(str(row))

    return '\n'.join(strings)


def transpose(matrix):
    result_matrix = Matrix((matrix.__len__()[1], matrix.__len__()[0]))

    for i in range(matrix.__len__()[0]):
        for j in range(matrix.__len__()[1]):
            result_matrix[j][i] = matrix[i][j]

    return result_matrix


class Matrix:
    def __init__(self, matrix, n=0):
        if isinstance(matrix, tuple):
            self.matrix = [[n for i in range(matrix[1])] for j in range(matrix[0])]

        else:
            self.matrix = matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.__len__() == other.__len__():
                result_matrix = Matrix(self.__len__())

                for i in range(self.__len__()[0]):
                    for j in range(self.__len__()[1]):
                        result_matrix[i][j] = self[i][j] + other[i][j]

                return result_matrix

            else:
                return None

        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.__len__() == other.__len__()[::-1]:
                result_matrix = Matrix((self.__len__()[0], other.__len__()[1]))

                for i in range(self.__len__()[0]):
                    for j in range(other.__len__()[1]):
                        for k in range(other.__len__()[0]):
                            result_matrix[i][j] += self.matrix[i][k] * other[k][j]

                return result_matrix

            else:
                return None

        else:
            return None

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        row = 0
        column = 0

        for r in self.matrix:
            row = row + 1

        for c in self.matrix[0]:
            column = column + 1

        size = row, column

        return size

    def __str__(self):
        return matrix_string(self.matrix)

    def __setitem__(self, item, element): # w celu przypisania elementów, do zamiany wierszy/kolumny w metodzie chio
        self.matrix[item] = element

#
# def main():
#     matrix = Matrix([[1, 0, 2], [-1, 3, 1]])
#     matrix_1 = Matrix((2, 3), 1)
#     matrix_2 = Matrix([[3, 1], [2, 1], [1, 0]])
#
#     print(transpose(matrix))
#
#     print('\n')
#     print(matrix + matrix_1)
#
#     print('\n')
#     print(matrix * matrix_2)
#
#
# main()
