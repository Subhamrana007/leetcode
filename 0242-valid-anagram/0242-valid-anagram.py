class Solution(object):
    def isAnagram(self, s, t):
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        return s_list == t_list

                
        """
        :type s: st
        :type t: str
        :rtype: bool
        """
        