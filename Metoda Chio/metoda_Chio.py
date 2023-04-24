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


def chio(tab: Matrix):
    n = tab.size()[0]
    if n == 2:
        return tab[0][0] * tab[1][1] - tab[0][1] * tab[1][0]
    mini_matrix = Matrix([[1 for _ in range(n - 1)] for _ in range(n - 1)])
    flag = False
    if tab[0][0] == 0:
        row = 0
        while tab[row][0] == 0:
            row += 1
        tmp = [0] * n
        for i in range(n):
            tmp[i] = tab[0][i]
            tab[0][i] = tab[row][i]
            tab[row][i] = tmp[i]
        flag = True
    for i in range(1, n):
        for j in range(1, n):
            mini_matrix[i - 1][j - 1] = tab[0][0] * tab[i][j] - tab[0][j] * tab[i][0]
    if flag:
        return -1 / (tab[0][0] ** (n - 2)) * chio(mini_matrix)
    return 1 / (tab[0][0] ** (n - 2)) * chio(mini_matrix)


A = Matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
print(chio(A))
B = Matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
print(chio(B))
C = Matrix([[0, -1, -5, 7, 9], [0, -7,5,34,32],[0,6,43,8,2],[30,3,5,2,0],[28,9,23,3,2]])
print(chio(C))