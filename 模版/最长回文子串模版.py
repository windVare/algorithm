

def longest_palindrome(string_):
    dp = [[0 for _ in range(len(string_))] for _ in range(len(string_))]

    max_len, start = 1, 0
    for i, x in enumerate(string_):
        for j, y in enumerate(string_[:i + 1]):
            # 初始化
            if i == j:
                dp[j][i] = False
            # 间距为1
            elif i - j == 1:
                dp[j][i] = x == y
            else:
                dp[j][i] = (dp[j + 1][i - 1] and x == y)

            if dp[j][i] and max_len < i - j + 1:
                max_len = i - j + 1
                start = j

    return string_[start: start + max_len]


if __name__ == '__main__':
    print(longest_palindrome("PATZJUJZTACCBCC"))
