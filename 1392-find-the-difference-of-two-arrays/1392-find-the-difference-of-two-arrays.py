class Solution(object):
    def findDifference(self, nums1, nums2):
        set_1 = set(nums1)
        set_2 = set(nums2)
        res_1 = set_1 - set_2
        res_2 = set_2 - set_1
        return [res_1,res_2]

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        