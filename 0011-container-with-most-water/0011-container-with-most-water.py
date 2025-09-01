class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = (len(height)-1)
        max_area = 0

        while i < (len(height)-1):
            area = (j-i) * min(height[i],height[j])

            if height[j] < height[i]:
                j -= 1

            else:
                i += 1

            if max_area < area:
                max_area = area

            

        return max_area
        
        

        

        