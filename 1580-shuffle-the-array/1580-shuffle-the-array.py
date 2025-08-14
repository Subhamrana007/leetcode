class Solution(object):
    def shuffle(self, nums, n):
        nums1 = nums[:n]
        nums2 = nums[n:]
        nums3 = []

        for i in range(n):
            nums3.append(nums1[i])
            nums3.append(nums2[i])
        return nums3

        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        