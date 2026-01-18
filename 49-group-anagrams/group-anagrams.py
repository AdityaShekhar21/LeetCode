class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        return list(anagrams.values())
