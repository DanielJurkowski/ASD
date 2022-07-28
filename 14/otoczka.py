from math import inf
from math import sqrt


def furthest_left(points):
    minimum_point = (inf, inf)
    minimum_index = inf
    for index, point in enumerate(points):
        if point[0] < minimum_point[0]:
            minimum_point = point
            minimum_index = index

        elif point[0] == points[minimum_index][0]:
            if point[1] < points[minimum_index][1]:
                minimum_point = point
                minimum_index = index

    return minimum_point, minimum_index


def orientation_check(point_1, point_2, point_3):
    value = (point_2[1] - point_1[1]) * (point_3[0] - point_2[0]) - \
            (point_2[0] - point_1[0]) * (point_3[1] - point_2[1])

    if value == 0:
        return 'collinear'

    if value > 0:
        return 'clockwise'

    if value < 0:
        return 'counter-clockwise'


def jarvis(points, flag=False):
    if len(points) < 3:
        return None

    result = []
    start_point, start_point_index = furthest_left(points)

    p, p_index = start_point, start_point_index

    while True:
        result.append(p)

        q, q_index = points[(p_index + 1) % len(points)], (p_index + 1) % len(points)

        for r_index, r in enumerate(points):
            orientation = orientation_check(p, r, q)

            if flag is True:
                if orientation == 'collinear':
                    distance_pq = sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
                    distance_pr = sqrt((r[0] - p[0]) ** 2 + (r[1] - p[1]) ** 2)
                    if distance_pr > distance_pq:
                        q = r

            if orientation == 'counter-clockwise':
                q = r
                q_index = r_index

        p = q
        p_index = q_index

        if p == start_point:
            break

    return result


def main():
    points_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    points_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    print('Pierwsza wersja algorytmu')
    print(jarvis(points_1))
    print(jarvis(points_2))
    print('')
    print(jarvis(points_3))

    print('\nDruga wersja algorytmu')
    print(jarvis(points_1, True))
    print(jarvis(points_2, True))
    print('')
    print(jarvis(points_3, True))


main()
