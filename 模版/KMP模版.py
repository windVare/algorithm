# https://www.cnblogs.com/dusf/p/kmp.html
# http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html


def get_next():
    j, k = 0, -1
    next_list[0] = -1

    while j < m:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            next_list[j] = k
        else:
            k = next_list[k]


def kmp():
    get_next()
    i, j = 0, 0
    while i < n:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]

        if j == m:
            return i

    return -1


if __name__ == '__main__':

    for p, s in [
        ["12313", "1212312313212"],
        ["12321", "1212312313212"]
    ]:
        n, m = len(s), len(p)
        next_list = [0 for _ in range(m + 1)]
        res = kmp()
        if res != -1:
            res = res - m + 1
        print(res)
