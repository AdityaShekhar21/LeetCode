class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for num in range(left, right + 1):
            bits = num.bit_count()   # fast built-in bit count
            if bits in primes:
                count += 1

        return count