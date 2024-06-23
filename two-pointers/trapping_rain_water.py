class Solution(object):
    '''
    HARD: 42
    Given n non-negative integers representing an elevation map where the 
    width of each bar is 1, compute how much water it can trap after raining.
    '''
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                lmax = max(lmax, height[left])
                ans += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                ans += rmax - height[right]
                right -= 1
        return ans