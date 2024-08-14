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
        # time - O(n), space - O(n)
        prefix_product = []
        curr_product = 1
        # compute prefix product
        for num in nums:
            prefix_product.append(curr_product)
            curr_product *= num
        curr_product = 1
        # compute final product inplace
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            nums[i] = curr_product * prefix_product[i]
            curr_product *= num
        return nums