class Element:
    def __init__(self, data, priority):
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

    def __str__(self):
        return str(self.priority) + " : " + str(self.data)


class Heap:
    def __init__(self, tab=None, size=0):
        if tab is None:
            tab = []
        self.tab = tab
        self.size = size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        m = i
        if l < self.size and self.tab[l].priority > self.tab[m].priority: m = l
        if r < self.size and self.tab[r].priority > self.tab[m].priority: m = r
        if m != i:
            self.tab[i], self.tab[m] = self.tab[m], self.tab[i]
            self.heapify(m)

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0].data

    def dequeue(self):
        if self.is_empty():
            return None
        self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
        self.size -= 1
        self.heapify(0)
        return self.tab.pop().data

    def enqueue(self, data, priority):
        self.tab.append(Element(data, priority))
        self.size += 1
        i = self.size - 1
        while i > 0 and self.tab[i].priority > self.tab[self.parent(i)].priority:
            self.tab[i], self.tab[self.parent(i)] = self.tab[self.parent(i)], self.tab[i]
            i = self.parent(i)

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

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


kol_prior = Heap()
t = [4, 7, 6, 7, 5, 2, 2, 1]
string = 'ALGORYTM'
for i in range(len(t)):
    kol_prior.enqueue(string[i], t[i])
kol_prior.print_tree(0, 0)
kol_prior.print_tab()
print(kol_prior.dequeue())
print(kol_prior.peek())
kol_prior.print_tab()
while not kol_prior.is_empty():
    print(kol_prior.dequeue())
kol_prior.print_tab()
