class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        N = [0] * (n + 1)
        Y = [0] * (n + 1)

        cnt = float('inf')
        ans = 0

        # Prefix count of 'N'
        for i in range(1, n + 1):
            if customers[i - 1] == 'N':
                N[i] = N[i - 1] + 1
            else:
                N[i] = N[i - 1]

        # Suffix count of 'Y'
        for i in range(n - 1, -1, -1):
            if customers[i] == 'Y':
                Y[i] = Y[i + 1] + 1
            else:
                Y[i] = Y[i + 1]

        # Find minimum penalty
        for i in range(n + 1):
            if N[i] + Y[i] < cnt:
                cnt = N[i] + Y[i]
                ans = i

        return ans