class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # Traverse from right to left (except first digit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                steps += 2      # +1 then /2
                carry = 1
            else:
                steps += 1      # just /2

        return steps + carry