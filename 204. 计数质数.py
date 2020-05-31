# 题目链接： https://leetcode-cn.com/problems/count-primes/


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0

        for i in range(2, n):
            j = i
            while i * j < n:
                is_primes[i * j] = 0
                j += 1

        return sum(is_primes)


if __name__ == '__main__':
    print(Solution().countPrimes(12))
