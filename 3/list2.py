class ListElement:
    size = 6

    def __init__(self):
        self.size = ListElement.size
        self.data_counter = 0
        self.next = None
        self.table = self.table = [None for x in range(self.size)]

    def add_helper(self, data, index):
        if all([self.data_counter != self.size, self.table[index] is None]):
            self.table[index] = data
            self.data_counter += 1

        elif all([self.data_counter != self.size, self.table[index] is not None]):
            # dodajemy element na dany indeks, resztę przesuwamy w prawo
            # wiemy, że lista nie jest pełna więc usuwamy jeden element None
            # z końca, żeby zachować rozmiar podstawowej tablicy
            self.table.insert(index, data)
            self.table.pop()
            self.data_counter += 1

        else:
            half_size = int(self.size / 2)  # potrzebujemy liczby całkowitej
            data_to_stay = self.table[:half_size]
            data_to_leave = self.table[half_size:]
            self.data_counter = len(data_to_leave)

            if index < half_size:
                data_to_stay.insert(index, data)
                data_to_leave.insert(0, data_to_stay.pop())

            else:
                data_to_leave.insert(index, data)

            self.table = data_to_stay + [None for x in range(half_size)]

            self.next = ListElement()

            for data in data_to_leave[:]:
                pass

    def delete_helper(self, index):
        if self.table[index] is not None:
            self.table[index] = None
            self.data_counter -= 1


class List:
    def __init__(self):
        self.head = ListElement()
        self.data_counter = 0

    def get(self, index):
        element_number = index // ListElement.size  # zwraca numer elementu
        # w którym jest indeks
        index_data = index % ListElement.size  # zwraca numer indeksu
        # w danym elemencie

        element = self.head
        element_counter = 0

        while element_counter != element_number:
            element = element.next
            element_counter += 1

        return element.table[index_data]

    def insert(self, data, index):
        element_number = index // ListElement.size
        index_data = index % ListElement.size

        element = self.head
        element_counter = 0

        while element_counter != element_number:
            element = element.next
            element_counter += 1

        element.add_helper(data, index_data)
        self.data_counter += 1

    def delete(self, index):
        pass

    def __str__(self):
        pass


def main():
    lista = List()
    lista.insert(1, 9)
    print(lista.get(3))


main()
