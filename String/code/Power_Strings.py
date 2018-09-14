def gen_pnext(p):
    j, k, m = 0, -1, len(p)
    pnext = [-1] * (m + 1)
    while j < m:
        if k == -1 or p[j] == p[k]:
            j, k = j + 1, k + 1
            pnext[j] = k
        else:
            k = pnext[k]
    return pnext

def PowerStrings(s):
    if len(s) % (len(s) - gen_pnext(s)[-1]) == 0:
        return int(len(s) / (len(s) - gen_pnext(s)[-1]))
    else:
        return 1
