from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        


        count = Counter(nums)             # Step 1: Count frequencies
        return [item for item, _ in count.most_common(k)]  # Step 2: Get top k

