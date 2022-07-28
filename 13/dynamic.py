from math import inf


def string_compare(P, T, i, j):
    if i == 0:
        return j

    if j == 0:
        return i

    switch = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    insertions = string_compare(P, T, i, j - 1) + 1
    deletes = string_compare(P, T, i - 1, j) + 1

    minimal_cost = min(switch, insertions, deletes)

    return minimal_cost


def string_compare_pd(P, T):
    lowest_costs = [[0 for _ in range(len(T))] for _ in range(len(P))]

    for i in range(len(T)):
        lowest_costs[0][i] = i

    for i in range(len(P)):
        lowest_costs[i][0] = i

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]

    for i in range(1, len(T)):
        parents[0][i] = 'I'

    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switch = (lowest_costs[i - 1][j - 1] + (P[i] != T[j]), 'S')
            insert = (lowest_costs[i][j - 1] + 1, 'I')
            delete = (lowest_costs[i - 1][j] + 1, 'D')

            minimal_cost = min([switch, insert, delete], key=lambda t: t[0])

            lowest_costs[i][j] = minimal_cost[0]

            if minimal_cost[1] != 'S':
                parents[i][j] = minimal_cost[1]

            elif minimal_cost[1] == 'S':
                parents[i][j] = 'M' if P[i] == T[j] else minimal_cost[1]

    return lowest_costs[len(P) - 1][len(T) - 1], parents


def reconstruct_path(parents):
    i, j = (len(parents) - 1, len(parents[0]) - 1)

    path = ''
    while parents[i][j] != 'X' and i >= 0 and j >= 0:
        if parents[i][j] == 'M':
            i -= 1
            j -= 1
            path = path + 'M'

        elif parents[i][j] == 'S':
            i -= 1
            j -= 1
            path = path + 'S'

        elif parents[i][j] == 'I':
            j -= 1
            path = path + 'I'

        elif parents[i][j] == 'D':
            i -= 1
            path = path + 'D'

    path = path[::-1]

    return path


def matching(P, T):
    lowest_costs = [[0 for _ in range(len(T))] for _ in range(len(P))]

    for i in range(len(P)):
        lowest_costs[i][0] = i

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switch = (lowest_costs[i - 1][j - 1] + (P[i] != T[j]), 'S')
            insert = (lowest_costs[i][j - 1] + 1, 'I')
            delete = (lowest_costs[i - 1][j] + 1, 'D')

            minimal_cost = min([switch, insert, delete], key=lambda t: t[0])

            lowest_costs[i][j] = minimal_cost[0]

            if minimal_cost[1] != 'S':
                parents[i][j] = minimal_cost[1]

    i = len(P) - 1
    j = 0

    for k in range(1, len(T)):
        if lowest_costs[i][k] < lowest_costs[i][j]:
            j = k

    # dodajemy jeden ze względu na spacje
    return j - i + 1


def longest_sequence(P, T):
    lowest_costs = [[0 for _ in range(len(T))] for _ in range(len(P))]

    for i in range(len(T)):
        lowest_costs[0][i] = i

    for i in range(len(P)):
        lowest_costs[i][0] = i

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]

    for i in range(1, len(T)):
        parents[0][i] = 'I'

    for i in range(1, len(P)):
        parents[i][0] = 'D'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            switch = (lowest_costs[i - 1][j - 1] + (inf if P[i] != T[j] else 0), 'S')
            insert = (lowest_costs[i][j - 1] + 1, 'I')
            delete = (lowest_costs[i - 1][j] + 1, 'D')

            minimal_cost = min([switch, insert, delete], key=lambda t: t[0])

            lowest_costs[i][j] = minimal_cost[0]

            if minimal_cost[1] != 'S':
                parents[i][j] = minimal_cost[1]

            elif minimal_cost[1] == 'S':
                parents[i][j] = 'M' if P[i] == T[j] else minimal_cost[1]

    path = reconstruct_path(parents)
    sequence = ''

    delete = 0
    for i in range(len(path)):
        if path[i] == 'M':
            sequence += T[i - delete + 1]

        if path[i] == 'D':
            delete += 1

    return sequence


def longest_monotone_sequence(T):
    sorted_T = sorted(T)

    P = ''
    for element in sorted_T:
        P += f'{element}'

    result = longest_sequence(P, T)

    return result


def main():
    P_1 = ' kot'
    T_1 = ' koń'

    P_2 = ' kot'
    T_2 = ' pies'

    P_3 = ' biały autobus'
    T_3 = ' czarny autokar'

    print(string_compare(P_1, T_1, len(P_1) - 1, len(T_1) - 1))
    print(string_compare(P_2, T_2, len(P_2) - 1, len(T_2) - 1))

    print(string_compare_pd(P_1, T_1)[0])
    print(string_compare_pd(P_2, T_2)[0])
    print(string_compare_pd(P_3, T_3)[0])

    P_4 = ' thou shalt not'
    T_4 = ' you should not'

    result = string_compare_pd(P_4, T_4)

    print(reconstruct_path(result[1]))

    P_5 = ' ban'
    T_5 = ' mokeyssbanana'

    print(matching(P_5, T_5))

    P_6 = ' democrat'
    T_6 = ' republican'

    print(longest_sequence(P_6, T_6))

    T_7 = ' 243517698'

    print(longest_monotone_sequence(T_7))


main()
