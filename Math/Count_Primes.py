# LeetCode 204 - Count Primes

# Difficulty: Medium
# Topic: Math / Number Theory / Sieve of Eratosthenes

class Solution:

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2

        while p * p < n:
            if is_prime[p]:
                for i in range(p * p, n, p):
                    is_prime[i] = False

            p += 1

        return sum(is_prime)


# Time Complexity: O(n log log n)
# Space Complexity: O(n)