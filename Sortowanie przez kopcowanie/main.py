from random import randint
from time import perf_counter


class Element:
    def __init__(self, priority, data=None):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other:
            return True
        return False

    def __gt__(self, other):
        if self.priority > other:
            return True
        return False

    def __repr__(self):
        if self.data != None:
            return str(self.priority) + " : " + str(self.data)
        return str(self.priority)


class Heap:
    def __init__(self, tab=None):
        if tab is None:
            tab = []
        self.tab = tab
        self.size = len(self.tab)
        self.buildheap()

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def heapify(self, n, i):
        l = self.left(i)
        r = self.right(i)
        m = i
        if l < n and self.tab[l].priority > self.tab[m].priority: m = l
        if r < n and self.tab[r].priority > self.tab[m].priority: m = r
        if m != i:
            self.tab[i], self.tab[m] = self.tab[m], self.tab[i]
            self.heapify(n, m)

    def buildheap(self):
        for i in range(self.parent(self.size - 1), -1, -1):
            self.heapify(self.size, i)

    def dequeue(self, i):
        if self.size > 0:
            self.tab[0], self.tab[i] = self.tab[i], self.tab[0]
            self.heapify(i, 0)

    def heapsort(self):
        for i in range(self.size - 1, 0, -1):
            self.dequeue(i)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.tab[i], end=', ')
        if self.size - 1 > -1 and self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx=0, lvl=0):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def TESTS():
    tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    tab_el = []
    for x in tab:
        tab_el.append(Element(x[0], x[1]))
    kopiec = Heap(tab_el)
    kopiec.print_tab()
    kopiec.print_tree()
    kopiec.heapsort()
    kopiec.print_tab()
    t = [Element(randint(0, 99)) for _ in range(1000)]
    t_start = perf_counter()
    kopiec_1 = Heap(t)
    kopiec_1.print_tab()
    kopiec_1.heapsort()
    kopiec_1.print_tab()
    t_stop = perf_counter()
    print('Czas obliczeń:', '{:.7f}'.format(t_stop - t_start))


TESTS()


class SelectionSort:
    def __init__(self, tab=None):
        if tab is None:
            tab = []
        self.tab = tab
        self.size = len(self.tab)

    def selection_swap(self):
        for i in range(self.size):
            min_idx = i
            for j in range(i + 1, self.size):
                if self.tab[min_idx].priority > self.tab[j].priority:
                    min_idx = j
            self.tab[i], self.tab[min_idx] = self.tab[min_idx], self.tab[i]

    def selection_shift(self):
        for i in range(self.size):
            min_idx = i
            for j in range(i + 1, self.size):
                if self.tab[min_idx].priority > self.tab[j].priority:
                    min_idx = j
            if i != min_idx:
                min_idx_ = self.tab.pop(min_idx)
                i_ = self.tab.pop(i)
                self.tab.insert(i, min_idx_)
                self.tab.insert(min_idx, i_)

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.tab[i], end=', ')
        if self.size - 1 > -1 and self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
        print('}')


def TESTS2():
    tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    tab_el = []
    for x in tab:
        tab_el.append(Element(x[0], x[1]))

    print("Swap")
    a = SelectionSort(tab_el.copy())
    a.selection_swap()
    a.print_tab()
    print("Shift")
    b = SelectionSort(tab_el.copy())
    b.selection_shift()
    b.print_tab()

    t_1 = [Element(randint(0, 99)) for _ in range(1000)]
    t_2 = t_1.copy()
    print("Swap")
    t_start = perf_counter()
    a = SelectionSort(t_1)
    a.selection_shift()
    a.print_tab()
    t_stop = perf_counter()
    print('Czas obliczeń:', '{:.7f}'.format(t_stop - t_start))
    print("Shift")
    t_start = perf_counter()
    a = SelectionSort(t_2)
    a.selection_shift()
    a.print_tab()
    t_stop = perf_counter()
    print('Czas obliczeń:', '{:.7f}'.format(t_stop - t_start))


TESTS2()
