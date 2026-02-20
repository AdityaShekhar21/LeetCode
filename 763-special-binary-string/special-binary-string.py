class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        blocks = []

        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1

            # found a special substring
            if count == 0:
                inner = s[start+1:i]
                # recursively optimize inside
                blocks.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1

        # sort descending for lexicographically largest
        blocks.sort(reverse=True)
        return "".join(blocks)