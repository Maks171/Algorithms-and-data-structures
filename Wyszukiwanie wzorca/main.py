import time
with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

def naive(S, W):
    m, i, ct = 0, 0, 0
    res = []
    while m + len(W) - 1 < len(S):
        ct += 1
        if S[m] == W[i]:
            copy = m
            while i < len(W) and S[m] == W[i]:
                ct += 2
                i += 1
                m += 1
            ct += 1
            if i == len(W):
                res.append(copy)
            m = copy
            i = 0
        m += 1
    print(len(res), ct, sep='; ')


t_start = time.perf_counter()
naive(S, 'the')
t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


def hash(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw * 256 + ord(word[i])) % 101
    return hw


def Rabin_Karp(S, W):
    M = len(S)
    N = len(W)
    res = []
    ct = 0
    hW = hash(W[:])
    for m in range(M - N + 1):
        hS = hash(S[m:m + N])
        ct += 1
        if hS == hW:
            if S[m:m + N] == W:
                res.append(m)
    print(len(res), ct, sep='; ')


t_start = time.perf_counter()
Rabin_Karp(S, 'the')
t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


def Rabin_Karp_rolling_hash(S, W):
    M = len(S)
    N = len(W)
    res = []
    ct, diff, h = 0, 0, 1
    for i in range(N - 1):
        h = (h * 256) % 101
    hW = hash(W[:])
    hS = hash(S[:N])
    ct += 1
    if hS == hW:
        if S[:N] == W:
            res.append(0)
        else:
            diff += 1

    for m in range(1, M - N):
        hS = (256 * (hS - ord(S[m - 1]) * h) + ord(S[m + N - 1])) % 101
        ct += 1
        if hS == hW:
            if S[m:m + N] == W:
                res.append(m)
            else:
                diff += 1
    print(len(res), ct, diff, sep='; ')


t_start = time.perf_counter()
Rabin_Karp_rolling_hash(S, 'the')
t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))


def kmp_table(W):
    T = [None] * (len(W) + 1)  # maksymalny rozmiar
    pos = 1
    cnd = 0
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos = pos + 1
        cnd = cnd + 1
    T[pos] = cnd
    return T


def kmp(S, W):
    T = kmp_table(W)
    ct = 0
    m = 0
    i = 0
    T = T.copy()
    P = []
    while m < len(S):
        ct += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - i)
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    print(len(P), ct, sep='; ')


t_start = time.perf_counter()
kmp(S, 'the')
t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}s".format(t_stop - t_start))
