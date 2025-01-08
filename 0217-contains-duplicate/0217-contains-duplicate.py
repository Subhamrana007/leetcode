class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sort the list
        nums.sort()
        
        # Check for duplicates by comparing adjacent elements
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True  # Duplicate found
        
        return False  # No duplicates

        