from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)

        for s in strs:
            character = [0]* 26

            for c in s:
                character[ord(c) - ord ("a")] +=1

            key = tuple(character)
            anagram[key].append(s)
        return anagram.values()


        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        