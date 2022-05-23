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


class Queue:
    def __init__(self, table=None):
        if table is None:
            self.table = []
            self.to_sort = False

        else:
            self.table = table
            self.table_sorted = []
            self.to_sort = True

    def is_empty(self):
        if len(self.table) == 0:
            return True

        else:
            return False

    def peek(self):
        if self.is_empty():
            return None

        else:
            data = self.table[0]

            return data

    def dequeue(self):
        if self.is_empty():
            if self.to_sort is False:
                return None

            else:
                if len(self.table_sorted) != 0:
                    self.table = self.table_sorted

                else:
                    return None

        else:
            self.table[0], self.table[-1] = self.table[-1], self.table[0]

            if self.to_sort is False:
                data = self.table.pop(-1)

            else:
                data = self.table.pop(-1)

                self.table_sorted.append(data)

            index = 0
            left_child_index = self.left(index)
            right_child_index = self.right(index)

            while (left_child_index < len(self.table) and right_child_index < len(self.table)) \
                    or (left_child_index < len(self.table) < right_child_index) \
                    or (left_child_index > len(self.table) > right_child_index):

                if self.table[left_child_index] < self.table[right_child_index]:
                    if self.table[index] < self.table[right_child_index]:
                        self.table[index], self.table[right_child_index] \
                            = self.table[right_child_index], self.table[index]

                        index = right_child_index
                        left_child_index = self.left(index)
                        right_child_index = self.right(index)

                    else:
                        break

                elif self.table[left_child_index] > self.table[right_child_index]:
                    if self.table[index] < self.table[left_child_index]:
                        self.table[index], self.table[left_child_index] \
                            = self.table[left_child_index], self.table[index]

                        index = left_child_index
                        left_child_index = self.left(index)
                        right_child_index = self.right(index)

                    else:
                        break

            return data

    def enqueue(self, element):
        self.table.append(element)

        index = len(self.table) - 1
        parent_index = self.parent(index)

        while self.table[index] > self.table[parent_index] and index != 0:
            self.table[index], self.table[parent_index] \
                = self.table[parent_index], self.table[index]

            index = parent_index
            parent_index = self.parent(index)

    def heapify(self):
        parent_index = self.parent(len(self.table) - 1)

        while parent_index >= 0:
            index = parent_index
            left_child_index = self.left(index)
            right_child_index = self.right(index)

            while (left_child_index < len(self.table) and right_child_index < len(self.table)) \
                    or (left_child_index < len(self.table) < right_child_index) \
                    or (left_child_index > len(self.table) > right_child_index):

                if self.table[left_child_index] < self.table[right_child_index]:
                    if self.table[index] < self.table[right_child_index]:
                        self.table[index], self.table[right_child_index] \
                            = self.table[right_child_index], self.table[index]

                        index = right_child_index
                        left_child_index = self.left(index)
                        right_child_index = self.right(index)

                    else:
                        break

                elif self.table[left_child_index] > self.table[right_child_index]:
                    if self.table[index] < self.table[left_child_index]:
                        self.table[index], self.table[left_child_index] \
                            = self.table[left_child_index], self.table[index]

                        index = left_child_index
                        left_child_index = self.left(index)
                        right_child_index = self.right(index)

                    else:
                        break

            parent_index -= 1

    @staticmethod
    def left(index):
        left_child_index = 2 * index + 1

        return left_child_index

    @staticmethod
    def right(index):
        right_child_index = 2 * index + 2

        return right_child_index

    @staticmethod
    def parent(index):
        parent_index = (index - 1) // 2

        return parent_index

    def print_table(self):
        print('{', end='')

        for i in range(len(self.table) - 1):
            print(self.table[i], end=', ')

        if not self.is_empty() and self.table[-1]:
            print(self.table[-1], end='')

        print('}')

    def print_tree(self, index, level):
        if index < len(self.table):
            self.print_tree(self.right(index), level + 1)
            print(2 * level * '  ', self.table[index] if self.table[index] else None)
            self.print_tree(self.left(index), level + 1)


def heap_sort_1():
    data_to_sort = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                    (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    for i, element in enumerate(data_to_sort):
        data_to_sort[i] = Element(element[1], element[0])

    table = Queue(data_to_sort)

    table.heapify()

    table.print_table()

    table.print_tree(0, 0)

    data = table.dequeue()

    while data is not None:
        data = table.dequeue()

    table.print_table()


def heap_sort_2():
    unsorted_list = [Element(None, int(random.random() * 100)) for i in range(10000)]

    t_start = time.perf_counter()

    table = Queue(unsorted_list)

    table.heapify()

    data = table.dequeue()

    while data is not None:
        data = table.dequeue()

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


heap_sort_1()
heap_sort_2()
