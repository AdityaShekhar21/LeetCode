class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trailing_zeros = []

        # Step 1: Count trailing zeros for each row
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        # Step 2: Try to place rows greedily
        for i in range(n):
            needed = n - i - 1
            j = i

            # Find row with enough trailing zeros
            while j < n and trailing_zeros[j] < needed:
                j += 1

            if j == n:
                return -1

            # Bubble it up
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = (
                    trailing_zeros[j - 1],
                    trailing_zeros[j],
                )
                swaps += 1
                j -= 1

        return swaps