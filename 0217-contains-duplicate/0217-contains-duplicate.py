class Solution(object):
    def containsDuplicate(self, nums):
        my_set= set()
        for i in range(len(nums)):
            if(nums[i] in my_set):
                return True
            else:
                my_set.add(nums[i])
                
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        