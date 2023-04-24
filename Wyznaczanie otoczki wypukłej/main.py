#skończone
from math import inf

lst1 = (0, 3), (0, 0), (0, 1), (3, 0), (3, 3)
lst2 = (0, 3), (0, 1), (0, 0), (3, 0), (3, 3)
lst3 = (2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)


def left_down_pt(lst):
    x_min = min(lst, key=lambda x: x[0])[0]
    y_min = inf
    for pt in lst:
        if pt[0] == x_min and pt[1] < y_min:
            y_min = pt[1]
    return lst.index((x_min, y_min))


def orientation(p, q, r):
    value = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if value == 0:
        return 0  # współliniowe
    elif value > 0:
        return 1  # prawoskrętne
    else:
        return 2  # lewoskrętne


def jarvis_algorithm(lst):
    idx = left_down_pt(lst)
    result = []
    p = idx
    while True:
        result.append(lst[p])
        q = (p + 1) % len(lst)
        for r in range(len(lst)):
            if orientation(lst[p], lst[r], lst[q]) == 2:
                q = r
        p = q
        if p == idx:
            break
    for i in result:
        print(i)


def jarvis_algorithm2(lst):
    idx = left_down_pt(lst)
    result = []
    p = idx
    while True:
        result.append(lst[p])
        q = (p + 1) % len(lst)
        r = q
        while r != p:
            if orientation(lst[p], lst[r], lst[q]) == 0 and \
                    (lst[p][0] < lst[q][0] < lst[r][0] or lst[p][0] > lst[q][0] > lst[r][0] or
                     lst[p][1] < lst[q][1] < lst[r][1] or lst[p][1] > lst[q][1] > lst[r][1]):
                q = r
            elif orientation(lst[p], lst[q], lst[r]) == 2:
                q = r
            r = (r + 1) % len(lst)
        p = q
        if p == idx:
            break
    for i in result:
        print(i)


jarvis_algorithm(lst1)
print(" ")
jarvis_algorithm(lst2)
print(" ")
jarvis_algorithm2(lst1)
print(" ")
jarvis_algorithm2(lst2)
print(" ")
print(" ")
jarvis_algorithm(lst3)
print(" ")
jarvis_algorithm2(lst3)
