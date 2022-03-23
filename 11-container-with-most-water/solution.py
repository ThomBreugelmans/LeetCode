class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        i = 0
        j = len(height)-1
        while i < j:
            water = (j-i) * min(height[i], height[j])
            max_water = max(max_water, water)
            if height[i] == height[j]:
                i+=1
                j-=1
            elif height[i] > height[j]:
                j-=1
            else:
                i+=1
                    
        return max_water