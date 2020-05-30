# 题目： 给定字符串， abc edf ghi jkl mno，反转为 mno jkl ghi edf abc。
# 要求： 不能使用内置的python字符串方法，不能创建新的变量对字符串进行存储，时间复杂度为O(n)，除常数空间外，不能新增其他的空间开销。


def reverse_str(array):
    i, j = 0, len(array) - 1

    start, end = -1, -1
    while i <= j:
        if array[i] and start == -1:
            start = i
        if (array[i] == ' ' and end == -1) or len(array) - 1 == i:
            if i != j:
                end = i - 1
            else:
                end = i

            # 单词反转
            while start < end:
                array[end], array[start] = array[start], array[end]
                start += 1
                end -= 1
            start, end = -1, -1

        i += 1

    # 字符串反转
    mid = len(array) // 2
    dis = 1
    while mid - dis >= 0 and mid + dis < len(array):
        array[mid - dis], array[mid + dis] = array[mid + dis], array[mid - dis]
        dis += 1
    # 边界值处理，长度为奇数或者偶数时，中间位置会存在偏移，导致第一个字符不能移位，需特殊处理。
    if mid - dis == 0 and mid + dis >= len(array):
        char = array.pop(0)
        array.append(char)

    return ''.join(array)


if __name__ == '__main__':
    print(reverse_str(list("abc  edf  g hi  jkl  mnop")))
    print(reverse_str(list("abc edf ghi jkl mnop")))
    print(reverse_str(list("abc edf ghi jkl mno")))
