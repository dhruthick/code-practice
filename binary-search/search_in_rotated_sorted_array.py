class Solution(object):
    '''
    33: MEDIUM
    Given the array nums after the possible rotation
    and an integer target, return the index of target
    if it is in nums, or -1 if it is not in nums.
    
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # time - O(logn), space - O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # at any point, either the left subarray or the right subarray is sorted.
            if nums[mid] == target:
                return mid
            # check if right subarray is sorted
            elif nums[mid] < nums[left]:
                # check if target is in right subarray
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # check if target is in left subarray
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                    
