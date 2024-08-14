class Solution(object):
    '''
    11: MEDIUM
    Find two lines that together with the x-axis form 
    a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # shrink pointers from either end according to highest height
        # time - O(n), space - O(1)
        left, right = 0, len(height) - 1
        max_volume = 0
        while left < right:
            max_volume = max(max_volume, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_volume