def KMP_Matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    pnext = gen_pnext(p)
    while i < m and j < n:
        if i == -1 or p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1

def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext
