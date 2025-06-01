class Solution(object):
    def twoSum(self, nums, target):
        empty = {}
        for i , n  in enumerate (nums):
            diff = target - nums[i];
            if diff in empty:
                return [empty[diff], i ]
            else:
                empty[n] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        