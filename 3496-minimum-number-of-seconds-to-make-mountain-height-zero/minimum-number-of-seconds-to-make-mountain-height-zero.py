import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        def can(t):
            total = 0
            for w in workerTimes:
                x = int((math.sqrt(1 + 8 * t / w) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False
        
        left, right = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        
        return left