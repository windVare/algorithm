# Author: wxs <wuxiushu@shiyedata.com>
# Date:   2020-05-06


def str_2_list(num_list, nums):
    while nums:
        num_list.insert(0, int(nums[0]))
        nums = nums[1:]

    return num_list


def list_2_str(num_list):
    string_ = ''
    num_list = num_list[::-1]
    ind = len(num_list)
    for index, number in enumerate(num_list):
        if number:
            ind = index
            break
    for number in num_list[ind:]:
        string_ += str(number)
    return string_


def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    num_list1, num_list2 = list(), list()
    str_2_list(num_list1, num1)
    str_2_list(num_list2, num2)

    num_list = [0 for _ in range(10 ** 5)]
    for index1, number1 in enumerate(num_list1):
        carry_bit = 0
        for index2, number2 in enumerate(num_list2):
            index = index1 + index2
            number = number1 * number2 + carry_bit + num_list[index]
            carry_bit = number // 10
            number = number % 10
            num_list[index] = number
        if carry_bit:
            num_list[index + 1] = carry_bit

    return list_2_str(num_list)


if __name__ == '__main__':
    print(multiply("123", "456"))
