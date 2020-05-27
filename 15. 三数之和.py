# 题目链接： https://leetcode-cn.com/problems/3sum/
# 解题思路： 固定一个数，然后双指针遍历，求和为0的三个数


class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return list()

        nums.sort()
        result_list = list()
        for x in range(length):
            if nums[x] > 0:
                return result_list

            # 重复数据过滤
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            y = x + 1
            z = length - 1
            while y < z:
                if nums[x] + nums[y] + nums[z] == 0:
                    result_list.append([nums[x], nums[y], nums[z]])
                    while y < z and nums[y] == nums[y + 1]:
                        y += 1
                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1
                    y += 1
                    z -= 1
                elif nums[x] + nums[y] + nums[z] > 0:
                    z -= 1
                else:
                    y += 1

        return result_list


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-2, 0, 0, 2, 2]))
