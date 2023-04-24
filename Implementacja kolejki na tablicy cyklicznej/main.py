class MyQueue:
    def __init__(self, size=5, save_index=0, read_index=0):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.save_index = save_index
        self.read_index = read_index

    def is_empty(self):
        if self.save_index == self.read_index:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            t = self.tab[self.read_index]
            self.tab[self.read_index] = None
            self.read_index = (self.read_index + 1) % self.size
            return t

    def enqueue(self, data):
        self.tab[self.save_index] = data
        self.save_index = (self.save_index + 1) % self.size
        if self.save_index == self.read_index:
            self.tab = realloc(self.tab, 2 * self.size)
            curr = self.read_index - 1
            new = self.size * 2 - 1
            while curr > -1:
                self.tab[curr], self.tab[new] = self.tab[new], self.tab[curr]
                curr -= 1
                new -= 1
            curr = self.size - 1
            while curr >= self.read_index:
                self.tab[curr], self.tab[new] = self.tab[new], self.tab[curr]
                curr -= 1
                new -= 1
            self.save_index = 0
            self.read_index = new + 1
            self.size = 2 * self.size

    def print_tab(self):
        print(self.tab)

    def print_queue(self):
        if self.is_empty():
            print([])
        i = self.read_index
        while i % self.size != self.save_index:
            print(self.tab[i % self.size], end=" ")
            i += 1
        print()


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


q = MyQueue()
for i in range(1, 5):
    q.enqueue(i)
print(q.dequeue())
print(q.peek())
q.print_queue()
for i in range(5, 9):
    q.enqueue(i)
q.print_tab()
while not q.is_empty():
    print(q.dequeue())
q.print_queue()
