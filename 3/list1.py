def realloc(table, size):
    old_size = len(table)

    return [table[i] if i < old_size else None for i in range(size)]


class queue:
    def __init__(self):
        self.actual_size = 5
        self.save_index = 0
        self.read_index = 0
        self.table = [None for x in range(self.actual_size)]

    def is_empty(self):
        if self.save_index == self.read_index:
            return True

        else:
            return None

    def peek(self):
        if self.is_empty():
            return None

        else:
            return self.table[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None

        else:
            dequeue_data = self.table[self.read_index]

            self.table[self.read_index] = None

            if self.read_index < self.actual_size - 1:
                self.read_index += 1

                return dequeue_data

            else:
                self.read_index = 0

                return dequeue_data

    def enqueue(self, data):
        self.table[self.save_index] = data

        if self.save_index < self.actual_size - 1:
            self.save_index += 1

        else:
            self.save_index = 0

        if self.save_index == self.read_index:
            table_size = self.actual_size

            realloc_size = 2 * table_size
            self.table = realloc(self.table, realloc_size)
            self.actual_size = realloc_size

            for i in range(self.save_index + 5, realloc_size):
                self.table[i] = self.table[i - table_size]
                self.table[i - table_size] = None

            self.read_index = table_size + 1

    def __str__(self):
        if self.is_empty():
            return 'Queue is empty'

        else:
            data_to_print = []

            for index in range(self.read_index, self.save_index):
                data_to_print.append(self.table[index])

            return str(data_to_print)

    def print_table(self):
        data_to_print = self.table

        print(data_to_print)


def main():
    queue_ = queue()

    for data in range(1, 5):
        queue_.enqueue(data)

    print(queue_.dequeue())

    print(queue_.peek())

    print(queue_)

    for data in range(5, 9):
        queue_.enqueue(data)

    queue_.print_table()

    data = queue_.dequeue()
    print(data)

    while data is not None:
        data = queue_.dequeue()

        if data is not None:
            print(data)
        else:
            pass

    print(queue_)


main()
