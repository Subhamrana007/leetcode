from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Initialize a defaultdict with list as the default factory
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to create a key
            sorted_word = ''.join(sorted(word))
            
            # Append the original word to the list associated with the sorted key
            anagrams[sorted_word].append(word)
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())



        