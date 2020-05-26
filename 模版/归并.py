def merge(left, right):
    """
    数组合并
    """
    result = list()

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result


def merge_sort(result):
    if len(result) < 2:
        return result

    mid = len(result) // 2

    return merge(merge_sort(result[:mid]), merge_sort(result[mid:]))


if __name__ == '__main__':
    print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(merge_sort())
