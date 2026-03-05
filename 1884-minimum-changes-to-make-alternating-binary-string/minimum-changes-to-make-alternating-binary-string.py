class Solution:
    def minOperations(self, s: str) -> int:
        changes_start_0 = 0
        changes_start_1 = 0

        for i, ch in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if ch != expected0:
                changes_start_0 += 1
            if ch != expected1:
                changes_start_1 += 1

        return min(changes_start_0, changes_start_1)