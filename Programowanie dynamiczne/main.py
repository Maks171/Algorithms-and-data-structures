import time
from math import inf


def string_compare(P, T, i, j):
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])
    zamian = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1

    najnizszy_koszt = min(zamian, wstawien, usuniec)
    return najnizszy_koszt


#P = ' kot'
#T = ' koń'
# _start = time.perf_counter()
#print(string_compare(P, T, len(P) - 1, len(T) - 1))
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


P = ' kot'
T = ' pies'
# t_start = time.perf_counter()
print(string_compare(P, T, len(P) - 1, len(T) - 1))
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


def string_compare_dp(P, T, pd=False, pr=False):
    D = [[0 for _ in range(len(P))] for __ in range(len(T))]
    for i in range(len(P)):
        D[0][i] = i
    for i in range(len(T)):
        D[i][0] = i

    parent = [['X' for _ in range(len(P))] for __ in range(len(T))]
    for i in range(1, len(P)):
        parent[0][i] = 'I'
    for i in range(1, len(T)):
        parent[i][0] = 'D'

    for i in range(1, len(T)):
        for j in range(1, len(P)):
            if P[j] == T[i]:
                D[i][j] = D[i - 1][j - 1]
                parent[i][j] = 'M'
                continue
            zamian = D[i - 1][j - 1] + (P[j] != T[i])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            if zamian < wstawien and zamian < usuniec:
                D[i][j] = zamian
                parent[i][j] = 'S'
            elif wstawien < usuniec:
                D[i][j] = wstawien
                parent[i][j] = 'I'
            else:
                D[i][j] = usuniec
                parent[i][j] = 'D'

    res = ''
    i = len(T) - 1
    j = len(P) - 1
    while parent[i][j] != 'X':
        res += parent[i][j]
        if parent[i][j] == 'M' or parent[i][j] == 'S':
            i -= 1
            j -= 1
        elif parent[i][j] == 'I':
            j -= 1
        else:
            i -= 1
    res = res[::-1]
    if pr is True:
        return res
    if pd is True:
        return D[-1][-1]


#P = ' kot'
#T = ' koń'
#print(string_compare_dp(P, T))

#P = ' kot'
#T = ' pies'
#print(string_compare_dp(P, T))

P = ' biały autobus'
T = ' czarny autokar'
print(string_compare_dp(P, T, pd=True))

P = ' thou shalt not'
T = ' you should not'
print(string_compare_dp(P, T, pr=True))


def fit_substring(P, T):
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawi = D[i][j - 1] + 1
            usunie = D[i - 1][j] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[i][j] = min_koszt
    j = 0
    for k in range(1, len(T)):
        if D[len(P) - 1][k] < D[len(P) - 1][j]:
            j = k
    return j - len(P) + 1

print(fit_substring('bin', 'mokeyssbanana'))

def nws(P, T):
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    parent = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
        parent[i][0] = 'D'
    for i in range(1, len(T)):
        D[0][i] = i
        parent[0][i] = 'I'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamian = inf
            else:
                zamian = D[i - 1][j - 1]
            wstawi = D[i][j - 1] + 1
            usunie = D[i - 1][j] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[i][j] = min_koszt
            if min_koszt == zamian and P[i] != T[j]:
                parent[i][j] = 'S'
            elif min_koszt == zamian and P[i] == T[j]:
                parent[i][j] = 'M'
            elif min_koszt == wstawi:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    i = len(P) - 1
    j = len(T) - 1
    elem = parent[i][j]
    path = ""
    while elem != 'X':
        path += elem
        if elem == 'S' or elem == 'M':
            i -= 1
            j -= 1
        elif elem == 'I':
            j -= 1
        elif elem == 'D':
            i -= 1
        elem = parent[i][j]

    path = path[::-1]
    result = ''
    i = 0
    for k in range(len(path)):
        if path[k] == 'D':
            i += 1
        elif path[k] == 'M':
            i += 1
            result += P[i]
    return result

print(nws('democrat', 'republican'))

def npm(T):
    P = sorted(T)
    P = "".join(P)
    if P[0] != ' ':
        P = ' ' + P
    if T[0] != ' ':
        T = ' ' + T
    D = [[0 for _ in range(len(T))] for __ in range(len(P))]
    parent = [['X' for _ in range(len(T))] for __ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
        parent[i][0] = 'D'
    for i in range(1, len(T)):
        D[0][i] = i
        parent[0][i] = 'I'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamian = inf
            else:
                zamian = D[i - 1][j - 1]
            wstawi = D[i][j - 1] + 1
            usunie = D[i - 1][j] + 1
            min_koszt = min(zamian, wstawi, usunie)
            D[i][j] = min_koszt
            if min_koszt == zamian and P[i] != T[j]:
                parent[i][j] = 'S'
            elif min_koszt == zamian and P[i] == T[j]:
                parent[i][j] = 'M'
            elif min_koszt == wstawi:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    i = len(P) - 1
    j = len(T) - 1
    elem = parent[i][j]
    path = ""
    while elem != 'X':
        path += elem
        if elem == 'S' or elem == 'M':
            i -= 1
            j -= 1
        elif elem == 'I':
            j -= 1
        elif elem == 'D':
            i -= 1
        elem = parent[i][j]
    path = path[::-1]
    result = ''
    i = 0
    for k in range(len(path)):
        if path[k] == 'D':
            i += 1
        elif path[k] == 'M':
            i += 1
            result += P[i]
    return result

print(npm('243517698'))
