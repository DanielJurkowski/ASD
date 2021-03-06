class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.table = [None for i in range(self.size)]

    def hash(self, key):
        if isinstance(key, int):
            modulo_result = key % self.size

            return modulo_result

        if isinstance(key, str):
            sum_ASCII = 0

            for character in key:
                sum_ASCII += ord(character)

            modulo_result = sum_ASCII % self.size

            return modulo_result

    def collision_delete(self, key, i):
        probing = (self.hash(key) + self.c1 * i + self.c2 * (i ** 2)) % self.size

        return probing

    def triple_hashing(self, i: int, key: int):
        # rozwiazanie mojego problemu
        return (self.hash(key) + i ** 3) % self.size

    def search(self, key):
        index = self.hash(key)

        i = 0
        while True:
            if i > self.size * 2:
                id_ = self.triple_hashing(key, i)

            if i >= self.size and None not in self.table:
                # przekroczenie ilosci miejsca
                break

            if self.table[index] is not None and self.table[index].key == key:
                data = self.table[index].data

                return data

            else:
                i += 1
                index = self.collision_delete(key, i)

        return None

    def insert(self, element):
        key = element.key
        index = self.hash(key)

        i = 0
        while i < self.size or None in self.table:
            if i >= self.size and None not in self.table:
                print('Brak miejsca')
                break

            if self.table[index] is None or self.table[index].key == key:
                self.table[index] = element
                break

            else:
                i += 1
                index = self.collision_delete(key, i)

    def remove(self, key):
        index = self.hash(key)

        i = 0
        while i < self.size:
            if self.table[index] is not None and self.table[index].key == key:
                self.table[index] = None
                break

            else:
                i += 1
                index = self.collision_delete(key, i)

        if i >= self.size:
            print('Brak danej')

    def __str__(self):
        string = '{'

        for element in self.table:
            if element is None:
                string += "None, "

            else:
                string += "{key}: {data}, ".format(key=element.key, data=element.data)

        string = string[:-2]
        string += '}'

        return string


def t_1(c1, c2):
    hash_table = HashTable(13, c1=c1, c2=c2)

    data = "ABCDEFGHIJKLMNO"

    for key, data in enumerate(data):
        if key + 1 != 6 and key + 1 != 7:
            element = Element(key + 1, data)
            hash_table.insert(element)

        elif key + 1 == 6:
            element = Element(18, data)
            hash_table.insert(element)

        elif key + 1 == 7:
            element = Element(31, data)
            hash_table.insert(element)

    print(hash_table)

    print(hash_table.search(5))

    print(hash_table.search(14))

    element = Element(5, 'Z')
    hash_table.insert(element)

    print(hash_table.search(5))

    hash_table.remove(5)

    print(hash_table)

    print(hash_table.search(31))

    element = Element('test', 'W')
    hash_table.insert(element)

    print(hash_table)


def t_2(c1, c2):
    hash_table = HashTable(13, c1=c1, c2=c2)

    data = "ABCDEFGHIJKLMNO"

    for key, data in enumerate(data):
        element = Element((key + 1) * 13, data)
        hash_table.insert(element)

    print(hash_table)


t_1(1, 0)
print('*' * 35)
t_2(0, 1)
# print('*'*35)
# t_1(0, 1)
