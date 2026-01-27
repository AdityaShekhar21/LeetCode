class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))

        return 1 + max_child_depth
