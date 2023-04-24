class Node:
    def __init__(self, key, value, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def _search_prev(self, node, key):
        if node is None or (node.left is None and node.right is None):
            return node
        if node.left is not None and node.left.key == key:
            return node
        if node.right is not None and node.right.key == key:
            return node
        if key > node.key:
            return self._search_prev(node.right, key)
        return self._search_prev(node.left, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        parent = self._search_prev(node, key)
        if parent is None:
            return None
        if parent.left is not None and parent.left.key == key:
            return parent.left
        if parent.right is not None and parent.right.key == key:
            return parent.right

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)

    def _insert(self, key, value, node):
        if node is None:
            return Node(key, value)
        if node.key == key:
            return Node(key, value, node.left, node.right)
        if key < node.key:
            node.left = self._insert(key, value, node.left)
            return node
        node.right = self._insert(key, value, node.right)
        return node

    def find_min(self, node):
        if node.left is None:
            return node
        while node.left.left is not None:
            node = node.left
        min = node.left
        if min.right is None:
            node.left = None
            return min
        node.left = min.right
        min.right = None
        return min

    def delete(self, key):
        return self._delete(self.root, key)

    def _delete(self, node, key):
        prev_to_delete = self._search_prev(node, key)

        if prev_to_delete is None and self.root.key != key:
            return None
        if self.root.key == key:
            to_delete = self.root
            add = self.find_min(to_delete.right)
            self.root = add
            add.right = to_delete.right
            add.left = to_delete.left

        elif prev_to_delete.left is not None and prev_to_delete.left.key == key:
            to_delete = prev_to_delete.left
            if to_delete.left is None and to_delete.right is None:
                prev_to_delete.left = None
            elif to_delete.left is None and to_delete.right is not None:
                prev_to_delete.left = to_delete.right
            elif to_delete.right is None and to_delete.left is not None:
                prev_to_delete.left = to_delete.left
            else:
                add = self.find_min(to_delete.right)
                prev_to_delete.left = add
                add.left = to_delete.left

        else:
            to_delete = prev_to_delete.right
            if to_delete.left is None and to_delete.right is None:
                prev_to_delete.right = None
            elif to_delete.left is None and to_delete.right is not None:
                prev_to_delete.right = to_delete.right
            elif to_delete.right is None and to_delete.left is not None:
                prev_to_delete.right = to_delete.left
            else:
                add = self.find_min(to_delete.right)
                prev_to_delete.right = add
                add.left = to_delete.left

    def make_string(self, node, t):
        if node is not None:
            self.make_string(node.left, t)
            t.append((node.key, node.value))
            self.make_string(node.right, t)

    def print(self):
        t = []
        self.make_string(self.root, t)
        print("{", end="")
        for x in range(len(t) - 1):
            print("{}:{}, ".format(t[x][0], t[x][1]), end="")
        print("{}:{}".format(t[-1][0], t[-1][1]), end="}\n")

    def height(self):
        return self._height(self.root)

    def _height(self, node, curr_height=1):
        if node is None:
            return curr_height - 1
        return max(curr_height, self._height(node.right, curr_height + 1), self._height(node.left, curr_height + 1))

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self._print_tree(node.left, lvl + 5)


BST = Tree()
BST.insert(50, 'A')
BST.insert(15, 'B')
BST.insert(62, 'C')
BST.insert(5, 'D')
BST.insert(20, 'E')
BST.insert(58, 'F')
BST.insert(91, 'G')
BST.insert(3, 'H')
BST.insert(8, 'I')
BST.insert(37, 'J')
BST.insert(60, 'K')
BST.insert(24, 'L')
BST.print_tree()
BST.print()
print(BST.search(24).value)
BST.insert(20, 'AA')
BST.insert(6, 'M')
BST.delete(62)
BST.insert(59, 'N')
BST.insert(100,'P')
BST.delete(8)
BST.delete(15)
BST.insert(55,'R')
BST.delete(50)
BST.delete(5)
BST.delete(24)
print(BST.height())
BST.print()
BST.print_tree()
