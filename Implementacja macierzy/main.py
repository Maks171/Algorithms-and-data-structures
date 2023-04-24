class Matrix:
    def __init__(self, lst, value=0):
        if isinstance(lst, tuple):
            self.__matrix = [[value for _ in range(lst[1])] for _ in range(lst[0])]
        else:
            self.__matrix = lst

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        output = "["
        for i in range(len(self.__matrix) - 1):
            output = output + str(self.__matrix[i]) + '\n'
        output = output + str(self.__matrix[-1]) + "]"
        return output

    def __add__(self, tab):
        if self.size() == tab.size():
            sum = Matrix((self.size()[0], self.size()[1]), 0)
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    sum[i][j] = self.__matrix[i][j] + tab.matrix[i][j]
            return sum
        else:
            raise ValueError

    def __mul__(self, tab):
        if self.size()[1] == tab.size()[0]:
            product = Matrix((self.size()[0], tab.size()[1]), 0)
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    for k in range(tab.size()[1]):
                        product[i][k] += self[i][j] * tab[j][k]
            return product
        else:
            raise ValueError


def transpose(tab: Matrix):
    transposed = Matrix((tab.size()[1], tab.size()[0]), 0)
    for i in range(tab.size()[0]):
        for j in range(tab.size()[1]):
            transposed[j][i] = tab[i][j]
    return transposed


A = Matrix([[1, 0, 2], [-1, 3, 1]])
A_tr = transpose(A)
print(A_tr)
B = Matrix((2, 3), 1)
C = Matrix([[3, 1], [2, 1], [1, 0]])
D = B * C
E = A_tr * D
print(D)

