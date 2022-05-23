import random
import time


class Element:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        if self.priority <= other.priority:
            return True

        else:
            return None

    def __gt__(self, other):
        if self.priority >= other.priority:
            return True

        else:
            return None

    def __str__(self):
        string = f'{self.priority} : {self.data}'

        return string

    def __repr__(self):
        return repr(f'{self.priority} : {self.data}')


def selection_sort_swap(data):
    for i in range(len(data)):
        minimum_index = i

        for j in range(i, len(data)):
            if data[j] < data[minimum_index]:
                minimum_index = j

        data[i], data[minimum_index] = data[minimum_index], data[i]

    return data


def selection_sort_shift(data):
    for i in range(len(data)):
        minimum_index = i

        for j in range(i, len(data)):
            if data[j] < data[minimum_index]:
                minimum_index = j

        data = data[:i] + data[minimum_index:minimum_index + 1] + data[i:minimum_index] + data[minimum_index + 1:]

    return data


def selection_1():
    data_to_sort = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                    (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    for i, element in enumerate(data_to_sort):
        data_to_sort[i] = Element(element[1], element[0])

    data = selection_sort_swap(data_to_sort)

    print(data)

    unsorted_list = [Element(None, int(random.random() * 100)) for i in range(10000)]

    t_start = time.perf_counter()

    sorted_list = selection_sort_swap(unsorted_list)

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def selection_2():
    data_to_sort = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                    (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    for i, element in enumerate(data_to_sort):
        data_to_sort[i] = Element(element[1], element[0])

    data = selection_sort_shift(data_to_sort)

    print(data)

    unsorted_list = [Element(None, int(random.random() * 1000)) for i in range(10000)]

    t_start = time.perf_counter()

    sorted_list = selection_sort_shift(unsorted_list)

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


selection_1()
selection_2()
