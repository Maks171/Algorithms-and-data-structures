class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTab:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def search(self, key):
        value = None
        for i in range(self.size):
            idx = self.probing(key, i)
            if self.tab[idx] is None:
                break
            elif self.tab[idx].key == key:
                value = self.tab[idx].value
                break
        return value

    def insert(self, key, value):
        flag = 0
        element = Element(key, value)
        if key is None:
            return None
        for i in range(self.size):
            idx = self.probing(key, i)
            if self.tab[idx] is None or self.tab[idx].value is None or self.tab[idx].key == key:
                self.tab[idx] = element
                flag = 1
                break
        if flag == 0:
            print("Brak miejsca")
            return None

    def remove(self, key):
        flag = 0
        for i in range(self.size):
            idx = self.probing(key, i)
            if self.tab[idx] is None:
                print("Brak danej")
                return None
            elif self.tab[idx].key == key:
                if self.tab[idx].value is not None:
                    self.tab[idx] = Element(key, None)
                    flag = 1
                break
        if flag == 0:
            print("Brak danej")
            return None

    def __str__(self):
        str = "{"
        for element in self.tab:
            if element is None or element.value is None:
                str += "None, "
            else:
                str += "{}:{}, ".format(element.key, element.value)
        str = str[:-2]
        str += "}"
        return str

    def hash(self, key):
        if isinstance(key, str):
            idx = (sum([ord(ch) for ch in key])) % self.size
        elif isinstance(key, int):
            idx = key % self.size
        else:
            raise ValueError
        return idx

    def probing(self, key, i=0):
        return (self.hash(key) + self.c1 * i + self.c2 * i ** 2) % self.size


def test1(c1, c2):
    T = 'ABCDEFGHIJKLMNOP'
    tab = HashTab(13, c1, c2)
    for i in range(15):
        if i == 6:
            tab.insert(18, T[i])
        elif i == 7:
            tab.insert(31, T[i])
        else:
            tab.insert(i, T[i])
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, 'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert('test', 'W')
    print(tab)


test1(1, 0)


def test2(c1, c2):
    T = 'ABCDEFGHIJKLMNOP'
    tab2 = HashTab(13, c1, c2)
    for i in range(1, 16):
        tab2.insert(13 * i, T[i - 1])
    print(tab2)

    tab2 = HashTab(13)
    for i in range(1, 16):
        tab2.insert(13 * i, T[i - 1])
    print(tab2)


test2(1, 0)
test2(0, 1)
test1(0, 1)
