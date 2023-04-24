class ListElements:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get(self):
        return self.data

    def __str__(self):
        return f"{self.data}"


class LinkedLists:
    def __init__(self):
        self.head = None

    def create(self, data):
        self.head = ListElements(data)

    def destroy(self):
        self.head = None

    def add(self, data):
        element = ListElements(data)
        element.next = self.head
        self.head = element

    def remove(self):
        if self.length() == 0:
            print("List is empty")
        elif self.length() == 1:
            self.head = None
        else:
            next_element = self.head.next
            self.head = next_element

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        count = 0
        head = self.head
        while head is not None:
            count += 1
            head = head.next
        return count

    def get(self):
        if self.head is None:
            raise ValueError
        return self.head.data

    def add_end(self, data):
        if self.head is None:
            self.head = ListElements(data)
        else:
            last_element = self.head
            while last_element.next is not None:
                last_element = last_element.next
            last_element.next = ListElements(data)

    def remove_end(self):
        if self.head.next is not None:
            next_to_last = self.head
            while next_to_last.next.next is not None:
                next_to_last = next_to_last.next
            next_to_last.next = None
        else:
            self.destroy()

    def __str__(self):
        if self.head is None:
            pass
        else:
            output = "["
            element = self.head
            while element is not None:
                if element.next is not None:
                    output += element.__str__() + ",\n"
                else:
                    output += element.__str__() + "]\n"
                element = element.next
            return output

    def take(self, n):
        lst = LinkedLists()
        if n > self.length():
            scope = self.length()
        else:
            scope = n
        element = self.head
        for i in range(scope):
            lst.add_end(element.data)
            element = element.next
        return lst

    def drop(self, n):
        lst = LinkedLists()
        if n < self.length():
            count = 0
            element = self.head
            for i in range(self.length()):
                if count >= n:
                    lst.add_end(element.data)
                element = element.next
                count += 1
            return lst
        else:
            return None


lst = LinkedLists()
lst.add(ListElements(("PR", "Warszawa", 1915)))
lst.add_end(ListElements(("UW", "Warszawa", 1915)))
lst.add(ListElements(("UJ", "Kraków", 1364)))
lst.add(ListElements(("AGH", "Kraków", 1919)))
lst.add(ListElements(("UP", "Poznań", 1919)))
lst2 = lst.drop(1)
lst2.add_end(ListElements(("UP", "Poznań", 1919)))
lst2.add_end(ListElements(("PG", "Gdańsk", 1945)))
lst2.add_end(ListElements(("PG", "Gdańsk", 1945)))
lst2.add_end(ListElements(("XX", "XX", 9999)))
lst3 = lst2.take(6)
print(lst3.__str__())




