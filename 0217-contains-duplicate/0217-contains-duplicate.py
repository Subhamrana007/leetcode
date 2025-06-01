class Solution(object):
    def containsDuplicate(self, nums):
        unique = set(nums)
        if(len(nums) == len(unique)):
            return False
        else:
            return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        