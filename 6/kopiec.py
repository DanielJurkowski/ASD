class Element:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other.priority:
            return True

        else:
            return None

    def __gt__(self, other):
        if self.priority > other.priority:
            return True

        else:
            return None

    def __str__(self):
        string = f'{self.priority} : {self.data}'

        return string


class Queue:
    def __init__(self):
        self.table = []

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
            return None

        else:
            self.table[0], self.table[-1] = self.table[-1], self.table[0]
            data = self.table.pop(-1)

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


def main():
    queue = Queue()

    data_to_sort = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
                    (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    for key, character in data_to_sort:
        queue.enqueue(Element(character, key))

    queue.print_tree(0, 0)

    queue.print_table()

    data_1 = queue.dequeue()
    print(data_1)

    data_2 = queue.peek()
    print(data_2)

    queue.print_tree(0, 0)

    queue.print_table()

    data_3 = queue.dequeue()

    while data_3 is not None:
        print(data_3)
        data_3 = queue.dequeue()

    queue.print_table()


main()
