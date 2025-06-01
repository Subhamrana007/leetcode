class Solution(object):
    def twoSum(self, nums, target):
        empty = {}
        for i in range(len(nums)):
            target1 = target - nums[i]
            if target1 in empty:
                return [empty[target1] , i]
            else:
                empty[nums[i]]= i
        

        