

def init(n, m):
    return [[0 for _ in range(n + 1)] for _ in range(m + 1)], [[0 for _ in range(n + 1)] for _ in range(m + 1)]


def lcs(s1, s2):
    dp, direction = init(len(s1), len(s2))
    for i, x in enumerate(s1, start=1):
        for j, y in enumerate(s2, start=1):
            if x == y:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = 1  # 左上角
            elif dp[i - 1][j] > dp[i][j - 1]:
                direction[i][j] = 2  # 左
                dp[i][j] = dp[i - 1][j]
            else:
                direction[i][j] = 3  # 上
                dp[i][j] = dp[i][j - 1]
    for d in dp:
        print(d)
    print('-' * 20)
    for d in direction:
        print(d)
    print("最长公共子序列的长度为：", dp[len(s1)][len(s2)])

    i, j = len(s1) - 1, len(s2) - 1
    lcs_list = list()
    while i >= 0 and j >= 0:
        if direction[i][j] == 1:
            i -= 1
            j -= 1
            lcs_list.append(s1[i])
        elif direction[i][j] == 2:
            i -= 1
        else:
            j -= 1
    print(lcs_list[::-1])


if __name__ == '__main__':
    lcs("ABCD", "BDCA")
    lcs("ABCPDSFJGODIHJOFDIUSHGD", "OSDIHGKODGHBLKSJBHKAGHI")
