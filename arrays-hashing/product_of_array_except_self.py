class Solution(object):
    """
    238: MEDIUM
    Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums
    except nums[i].
    The product of any prefix or suffix of nums is guaranteed to
    fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without
    using the division operation.
    Can you solve the problem in O(1) extra space complexity?
    (The output array does not count as extra space for space
    complexity analysis.)
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # compute product of all left numbers
        answer = [1] * len(nums)
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i - 1]
            answer[i] = temp
        temp = 1
        # multiply answer with product of all right numbers
        for i in reversed(range(len(nums) - 1)):
            temp *= nums[i + 1]
            answer[i] *= temp
        return answer