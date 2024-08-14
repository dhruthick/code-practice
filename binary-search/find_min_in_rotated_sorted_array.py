class Solution(object):
    '''
    153: MEDIUM
    Given the sorted rotated array nums of unique 
    elements, return the minimum element of this array.
    '''
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time - O(logn), space - O(1)
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
