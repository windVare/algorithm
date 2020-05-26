

def calc(n):
    result_list = [[0 for _ in range(n)] for _ in range(n)]
    result_list[0][0], result_list[1][0], result_list[1][1] = 1, 1, 1
    for i in range(2, n):
        for j in range(i + 1):
            if j == 0 or j == i:
                result_list[i][j] = 1
            else:
                result_list[i][j] = result_list[i - 1][j] + result_list[i - 1][j - 1]

    return result_list


if __name__ == '__main__':
    data_list = calc(10)
    for i in range(10):
        print(data_list[i][:i + 1])
