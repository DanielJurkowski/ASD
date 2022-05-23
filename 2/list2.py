class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


# funkcje bazowe
def nil():
    element = Element(None)

    return element


def cons(element, list):
    list, list.next = Element(element), list

    return list


def first(list):
    first = list.data

    return first


def rest(list):
    rest = list.next

    return rest


# reszta funkcji
def create():
    return nil()


def destroy():
    return nil()


def add(element, list):
    return cons(element, list)


def remove(list):
    if is_empty(list):
        pass

    else:
        return rest(list)


# obserwatory
def is_empty(list):
    if first(list) is None:
        return True

    else:
        return False


def length(list):
    if is_empty(list):
        return 0

    else:
        list_length = 1 + length(rest(list))

        return list_length


def get(list):
    return first(list)


# dodatkowe funkcje
def print_list(list, string=''):
    if is_empty(list):
        string_to_print = string[0:(len(string) - len(', '))]

        if string != '':
            print(string_to_print)

        else:
            print('List is empty')

    else:

        print_list(rest(list), string + str(first(list)) + ', ')


def add_end(element, list):
    # zaimplementowane zgodnie z kodem z upela
    if is_empty(list):
        return add(element, list)

    else:
        first_element = first(list)
        rest_list = rest(list)
        recreated_list = add_end(element, rest_list)

        return add(first_element, recreated_list)


def remove_end(list):
    if is_empty(rest(list)):
        empty_list = create()

        return empty_list

    else:
        first_element = first(list)
        rest_list = rest(list)

        return add(first_element, remove_end(rest_list))


def take(n, list):
    if n == 1:
        first_element = first(list)
        empty_list = create()

        return add(first_element, empty_list)

    else:
        first_element = first(list)
        rest_list = rest(list)

        return add(first_element, take(n - 1, rest_list))


def drop(n, list):
    if n == 0:
        return list

    else:
        return drop(n - 1, remove(list))


def main():
    elements = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]

    # utworzenie listy, oraz sprawdzenie operacji dodawania na początek
    List = create()

    for element in elements:
        # jest na odwrót niż w liście krotek ale wystarczy zamienic tu na add_end
        List = add(element, List)

    # sprawdzenie wypisania listy
    print_list(List)

    # sprawdzenie usunięcia z początku listy
    List = remove(List)
    print('\n')
    print_list(List)

    # sprawdzenie obserwatora get
    first_element = get(List)
    print('\n')
    print(first_element)

    # sprawdzenie obserwatora length, is_empty jest używany w funkcjach
    list_length = length(List)
    print('\n')
    print(list_length)

    # sprawdzenie usunięcia z końca listy
    List = remove_end(List)
    print('\n')
    print_list(List)

    # sprawdzenie dodania na koniec listy
    List = add_end(('AGH', 'Kraków', 1919), List)
    print('\n')
    print_list(List)

    # sprawdzenie tworzenia listy z n pierwszych elementów
    List = take(3, List)
    print('\n')
    print_list(List)

    # sprawdzenie tworzenia listy przez usuniecie n pierwszych elementów
    List = drop(2, List)
    print('\n')
    print_list(List)

    # sprawdzenie usunięcia listy
    List = destroy()
    print('\n')
    print_list(List)


main()
