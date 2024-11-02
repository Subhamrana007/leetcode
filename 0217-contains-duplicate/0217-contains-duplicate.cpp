#include <algorithm>
#include <vector>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 1; i++) { // Iterate only up to the second-to-last element
            if (nums[i] == nums[i + 1]) { // Check consecutive elements for duplicates
                return true; // Duplicate found
            }
        }
        
        return false; // No duplicates found
    }
};
