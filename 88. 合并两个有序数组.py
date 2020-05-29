# 题目链接：https://leetcode-cn.com/problems/merge-sorted-array/
# 解题思路：逆序处理，从后往前，大的数后移


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[length] = nums1[m]
                m -= 1
            else:
                nums1[length] = nums2[n]
                n -= 1
            length -= 1

        while n >= 0:
            nums1[length] = nums2[n]
            length -= 1
            n -= 1

        return nums1


if __name__ == '__main__':
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
