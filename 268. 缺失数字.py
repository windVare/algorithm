# 题目链接： https://leetcode-cn.com/problems/missing-number/
# 解题思路： 等差数列求和


class Solution:
    def missingNumber(self, nums) -> int:
        length = len(nums) + 1
        s = (length - 1) * length / 2
        return int(s - sum(nums))


if __name__ == '__main__':
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(Solution().missingNumber([3, 0, 1]))
