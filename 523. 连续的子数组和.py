class Solution:
    """
    选择数组区间即可
    """

    def checkSubarraySum(self, nums, k) -> bool:
        if len(nums) < 2:
            return False

        if k == 0:
            for i in range(len(nums)):
                if i == 0:
                    continue
                if nums[i] + nums[i - 1] == 0:
                    return True
            return False

        data_list = list()
        for index, num in enumerate(nums):
            if index == 0:
                data_list.append(num)
            else:
                data_list.append(num + data_list[index - 1])

        for indx in range(len(data_list)):
            if indx >= 1 and data_list[indx] % k == 0:
                return True
            for indy in range(indx - 1):
                d = data_list[indx] - data_list[indy]
                if d % k == 0:
                    return True

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 25))
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 0))
