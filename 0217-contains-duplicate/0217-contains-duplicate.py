class Solution(object):
    def containsDuplicate(self, nums):
        emt_set = set()
        for n in nums:
            if n in emt_set:
                return True
            emt_set.add(n)
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        