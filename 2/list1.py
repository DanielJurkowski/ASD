from copy import deepcopy


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # transformatory
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, element):
        new_element = Element(element)

        if self.is_empty():
            self.head = new_element

        else:
            self.head, new_element.next = new_element, self.head

    def remove(self):
        self.head = self.head.next

    # obserwatory
    def is_empty(self):
        if self.head is None:
            return True

        else:
            return False

    def length(self):
        counter = 0

        if self.is_empty():
            return counter

        else:
            element = self.head

            while element.next:
                counter += 1
                element = element.next

            counter += 1

            return counter

    def get(self):
        if self.is_empty():
            return str('List is empty')

        else:
            element_to_get = self.head

            return element_to_get.data

    # dodatkowe
    def __str__(self):
        if self.is_empty():
            return 'List is empty'

        else:
            print_value = self.head
            string = ''

        while print_value.next is not None:
            string += str(print_value.data) + ', '
            print_value = print_value.next

        string += str(print_value.data)

        return string

    def add_end(self, element):

        if self.is_empty():
            self.head = Element(element)

        else:
            element_to_add = Element(element)

            last = self.head

            while last.next is not None:
                last = last.next

            last.next = element_to_add

    def remove_end(self):
        if self.is_empty():
            pass

        elif self.length() == 1:
            self.head = None

        else:
            last = self.head
            element = self.head

            while last.next is not None:
                last = last.next

            while element.next is not last:
                element = element.next

            element.next = None

    def take(self, n):
        if n >= self.length():
            new_list = LinkedList()

            new_list = deepcopy(self)

            return new_list

        else:
            counter = 0

            new_list = LinkedList()
            element = self.head

            while counter < n:
                new_list.add_end(element.data)

                element = element.next

                counter += 1

            return new_list

    def drop(self, n):
        if n >= self.length():
            new_list = LinkedList()

            return new_list

        elif n < 0:
            new_list = deepcopy(self)

            return new_list

        else:
            new_list = deepcopy(self)
            counter = 0
            element = self.head

            while element is not None and counter != n:
                element = element.next
                counter += 1

                if counter == n:
                    break

            if counter == 0:
                return new_list

            else:
                for i in range(counter):
                    new_list.remove()

                return new_list


def main():
    elements = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]

    # utworzenie listy, oraz sprawdzenie operacji dodawania na początek
    Linked_List = LinkedList()

    for element in elements:
        Linked_List.add(element)

    # sprawdzenie wypisania listy
    print(Linked_List)

    # sprawdzenie usunięcia z początku listy
    Linked_List.remove()
    print('\n', Linked_List)

    # sprawdzenie obserwatora get, reszta obserwatorów została użyta w implementacji innych funkcji
    print('\n', Linked_List.get())

    # sprawdzenie usunięcia z końca listy
    Linked_List.remove_end()
    print('\n', Linked_List)

    # sprawdzenie dodania na koniec listy
    Linked_List.add_end(('AGH', 'Kraków', 1919))
    print('\n', Linked_List)

    # sprawdzenia tworzenia listy z n pierwszych elementów
    new_list_1 = Linked_List.take(3)
    print('\n', new_list_1)
    print('\n', Linked_List)

    # sprawdzenia tworzenia listy przez usunięcie n pierwszych elementów
    new_list_2 = Linked_List.drop(3)
    print('\n', new_list_2)
    print('\n', Linked_List)

    # sprawdzenie usunięcia listy
    Linked_List.destroy()
    print('\n', Linked_List)


main()
