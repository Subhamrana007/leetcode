class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow_pointer = 0
        fast_pointer = 0
        for fast_pointer in range(len(nums)):
            if nums[fast_pointer] != 0:
                nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]
                slow_pointer += 1



        """
        Do not return anything, modify nums in-place instead.
        """
        