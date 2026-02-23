class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == (1 << k):  # 2^k
                return True

        return len(seen) == (1 << k)