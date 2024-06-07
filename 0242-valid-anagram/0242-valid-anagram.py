class Solution(object):
    def isAnagram(self, s, t):
        return  sorted(list(s))== sorted(list(t))

                
        """
        :type s: st
        :type t: str
        :rtype: bool
        """
        