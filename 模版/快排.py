def split(arr, low, high):
    """
    单指针遍历法
    """
    # i 指向比较元素的期望位置
    i = low
    # 将该数组第一个元素设置为比较元素
    x = arr[i]
    # 从数组的第二个元素起开始遍历，若找到的元素大于比较元素，则跳过
    j = low + 1
    while j <= high:
        # 若找到了小于比较元素的数，则将其与前面较大的数进行交换
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    # 将比较元素交换到期望位置
    arr[low], arr[i] = arr[i], arr[low]
    return i


def partition(arr, low, high):
    """
    双指针遍历法
    """
    # 将该数组第一个元素设置为比较元素
    x = arr[low]
    # i 指向数组头的指针
    # j 指向数组尾的指针
    i, j = low, high

    while i < j:
        # 从右至左找到第一个小于比较元素的数
        while i < j and arr[j] >= x:
            j -= 1
        # 从左至右找到第一个大于比较元素的数
        while i < j and arr[i] <= x:
            i += 1

        # NOTE 这里的 j - 1 与 i + 1 的顺序不可以调换。如果调换了顺序，i会走过头，以至于将后面较大的元素交换到数组开头

        # 将大数与小数交换
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]

    # 将比较元素交换到期望位置
    arr[low], arr[i] = arr[i], arr[low]
    return i


def quick_sort(arr, low, high):
    if low < high:
        # i = partition(arr, low, high)
        i = split(arr, low, high)
        quick_sort(arr, low, i - 1)
        quick_sort(arr, i + 1, high)


if __name__ == '__main__':
    array_list = [5, 7, 1, 6, 4, 8, 3, 2]
    quick_sort(array_list, 0, 7)
    print(array_list)
