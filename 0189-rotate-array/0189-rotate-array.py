class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, front, rear):
            while front < rear:
                nums[front], nums[rear] = nums[rear], nums[front]
                front += 1
                rear -= 1
            
        k = k % len(nums)
        
        if k > len(nums):
            return

        

        reverse(nums, 0, len(nums)-1 )
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
        """
        Do not return anything, modify nums in-place instead.
        """
        