from matrix import Matrix as Matrix
from copy import deepcopy as deepcopy


def chio_det(matrix):
    if matrix.__len__()[0] == matrix.__len__()[1]:
        n = matrix.__len__()[0]
        swapped = False

        copy_matrix = deepcopy(matrix)

        if copy_matrix[0][0] == 0:  # w celu usunięcia 0 z pierwszego miejsca zamieniamy kolumnę/wiersz,
            # jeżeli nie będzie takiej z którą możemy zamienić, to oznacza to, że występują tam same zera
            # czyli wyznacznik jest równy 0
            for i in range(n - 1):
                if copy_matrix[i][0] != 0:
                    copy_matrix[0], copy_matrix[i] = copy_matrix[i], copy_matrix[0]
                    swapped = True

                    break

                elif copy_matrix[0][i] != 0:
                    for j in range(n - 1):
                        copy_matrix[j][i], copy_matrix[0][i] = copy_matrix[0][i], copy_matrix[j][i]
                        swapped = True

                        break
            else:
                return 0

        while n > 2:
            temp_matrix = Matrix(((n - 1), (n - 1)))

            for i in range(n - 1):
                for j in range(n - 1):
                    temp_matrix[i][j] = (copy_matrix[0][0] * copy_matrix[i + 1][j + 1] -
                                         copy_matrix[0][j + 1] * copy_matrix[i + 1][0])

            for i in range(n - 1):  # mnożymy cały wyznacznik przez stała, czyli dowolny wiersz/kolumnę przez tą stałą
                temp_matrix[0][i] = (1 / (copy_matrix[0][0] ** (n - 2))) * temp_matrix[0][i]

            copy_matrix = temp_matrix
            n = n - 1

        det = (copy_matrix[0][0] * copy_matrix[1][1] - copy_matrix[0][1] * copy_matrix[1][0])

        if swapped:
            return -det

        else:
            return det

    else:
        return None


def main():
    matrix = Matrix([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])

    matrix_1 = Matrix([
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])

    print(chio_det(matrix))
    print(chio_det(matrix_1))


main()
