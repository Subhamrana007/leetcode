class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty ={}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in empty:
                return [i,nums.index(diff)]
            else:
                empty[num] = i