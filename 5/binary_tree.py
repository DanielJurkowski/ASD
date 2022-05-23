from copy import deepcopy


class ChildNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None


class RootNode:
    def __init__(self):
        self.head = None

    # wyszukiwanie w drzewie
    def search(self, key):
        if self.head is not None:
            return self.search_helper(key, self.head)

        else:
            return None

    def search_helper(self, key, node):
        if node.key == key:
            return node.value

        elif key < node.key and node.left is not None:
            return self.search_helper(key, node.left)

        elif key > node.key and node.right is not None:
            return self.search_helper(key, node.right)

        else:
            return None

    # wstawianie do drzewa
    def insert(self, key, value):
        if self.head is None:
            self.head = ChildNode(key, value)

        else:
            self.insert_helper(key, value, self.head)

    def insert_helper(self, key, value, node):
        if key < node.key:
            if node.left is not None:
                if node.left.key == key:
                    node.left.value = value

                else:
                    self.insert_helper(key, value, node.left)

            else:
                node.left = ChildNode(key, value)

        if key > node.key:
            if node.right is not None:
                if node.right.key == key:
                    node.right.value = value

                else:
                    self.insert_helper(key, value, node.right)

            else:
                node.right = ChildNode(key, value)

    # usuwanie z drzewa
    def delete(self, key):
        if self.head is None:
            pass

        else:
            if key == self.head.key:
                if self.head.left is None and self.head.right is None:
                    self.head = None

                elif (self.head.left is None and self.head.right is not None) \
                        or (self.head.left is not None and self.head.right is None):
                    if self.head.left is not None:
                        self.head = self.head.left

                    if self.head.right is not None:
                        self.head = self.head.right

                else:
                    minimum_node = self.search_minimum(self.head.right)
                    temp_node = deepcopy(minimum_node)

                    self.delete(minimum_node.key)
                    self.head, temp_node.left, temp_node.right = temp_node, self.head.left, self.head.right

            else:
                self.delete_helper(key, self.head)

    def delete_helper(self, key, node):
        if key < node.key:
            if node.left is not None:
                if node.left.key == key:
                    if node.left.left is None and node.left.right is None:
                        node.left = None

                    elif (node.left.left is None and node.left.right is not None) \
                            or (node.left.left is not None and node.left.right is None):
                        if node.left.left is not None:
                            node.left = node.left.left

                        if node.left.right is not None:
                            node.left = node.left.right

                    else:
                        minimum_node = self.search_minimum(node.left.right)

                        node.left, minimum_node.left = minimum_node, node.left.left

                else:
                    self.delete_helper(key, node.left)

            else:
                pass

        if key > node.key:
            if node.right is not None:
                if node.right.key == key:
                    if node.right.left is None and node.right.right is None:
                        node.right = None

                    elif (node.right.left is None and node.right.right is not None) \
                            or (node.right.left is not None and node.right.right is None):
                        if node.right.left is not None:
                            node.right = node.right.left

                        if node.right.right is not None:
                            node.right = node.right.right

                    else:
                        minimum_node = self.search_minimum(node.right.right)

                        node.right, minimum_node.left = minimum_node, node.right.left

                else:
                    self.delete_helper(key, node.right)

            else:
                pass

        else:
            pass

    # minimum poddrzewa
    def search_minimum(self, node):
        if node.left is not None:
            return self.search_minimum(node.left)

        else:
            return node

    # wysokości drzewa
    def height(self):
        if self.head is not None:
            return self.height_helper(self.head)

        else:
            pass

    def height_helper(self, node):
        if node.left is not None and node.right is not None:
            height = 1 + max(self.height_helper(node.left),
                             (self.height_helper(node.right)))

            return height

        elif node.left is not None:
            height = 1 + self.height_helper(node.left)

            return height

        elif node.right is not None:
            height = 1 + self.height_helper(node.right)

            return height

        else:
            height = 1

            return height

    # przechodzenie drzewa w kolejności
    def traverse_inorder(self):
        if self.head is not None:
            return self.traverse_inorder_helper(self.head)

        else:
            return None

    def traverse_inorder_helper(self, node, data=None):
        if data is None:
            data = []

        if node.left is not None:
            self.traverse_inorder_helper(node.left, data=data)

        data.append((node.key, node.value))

        if node.right is not None:
            self.traverse_inorder_helper(node.right, data=data)

        return data

    # wypisanie drzewa
    def print(self):
        print("==============")
        self.print_helper(self.head, 0)
        print("==============")

    def print_helper(self, node, level):
        if node is not None:
            self.print_helper(node.right, level + 5)

            print()
            print(level * " ", node.key, node.value)

            self.print_helper(node.left, level + 5)


def main():
    tree = RootNode()

    data = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F',
            91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}

    for key, value in data.items():
        tree.insert(key, value)

    tree.print()

    print(tree.traverse_inorder())

    print(tree.search(24))

    tree.insert(20, 'AA')

    tree.insert(6, 'M')

    tree.delete(62)

    tree.insert(59, 'N')

    tree.insert(100, 'P')

    tree.delete(8)

    tree.delete(15)

    tree.insert(55, 'R')

    tree.delete(50)

    tree.delete(5)

    tree.delete(24)

    print(tree.height())

    print(tree.traverse_inorder())

    tree.print()


main()
