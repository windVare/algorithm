class Solution:
    def maxSubArray(self, nums) -> int:
        m = s = nums[0]
        for i in range(1, len(nums)):
            if s >= 0:
                s += nums[i]
            else:
                s = nums[i]

            if s > m:
                m = s

        return m


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
