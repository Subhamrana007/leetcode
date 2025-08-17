class Solution(object):
    def twoSum(self, nums, target):
        empty = {}
        for i,n in enumerate (nums):
            diff = target - n
            if diff in empty:
                return[ i ,empty[diff]]
            else:
                empty[n] = i 

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        