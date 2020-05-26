

def LIS(res):
    dp = [0 for _ in range(len(res))]
    dp[0] = 1

    for i, x in enumerate(res):
        maxx = 1
        for j, y in enumerate(res):
            if j >= i:
                break
            if x > y:
                maxx = max(dp[j] + 1, maxx)
        dp[i] = maxx

    return max(dp)


if __name__ == '__main__':
    print(LIS([4, 2, 3, 1, 5]))
    print(LIS([10, 9, 2, 5, 3, 7, 101, 18]))
