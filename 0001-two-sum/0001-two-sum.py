class Solution(object):
    def twoSum(self, nums, target):
        new_hash= {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in new_hash:
                return[new_hash[diff], i]
            new_hash[n]= i
        return

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        