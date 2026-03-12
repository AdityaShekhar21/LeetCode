class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True


class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            optional = []

            # mandatory edges
            for u, v, s, must in edges:
                if must:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False
                    used += 1
                else:
                    optional.append((u, v, s))

            normal = []
            upgrade = []

            for u, v, s in optional:
                if s >= x:
                    normal.append((u, v))
                elif s * 2 >= x:
                    upgrade.append((u, v))

            for u, v in normal:
                if dsu.union(u, v):
                    used += 1

            for u, v in upgrade:
                if used == n-1:
                    break
                if upgrades == k:
                    break
                if dsu.union(u, v):
                    upgrades += 1
                    used += 1

            return used == n-1

        lo, hi = 0, max(s*2 for _,_,s,_ in edges)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans