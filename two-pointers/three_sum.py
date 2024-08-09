class Solution(object):
    '''
    15: MEDIUM
    Find all triplets that sum to zero in an array.
    No duplicates.
    '''
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Two Sum II approach
        answers = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # array is sorted so no more pairs will be found if > 0
            if nums[i] > 0:
                break
            # to avoid duplicates
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            # two sum II
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                twosum = nums[left] + nums[right]
                if twosum == target:
                    answers.append((nums[left], nums[right], nums[i]))
                    left += 1
                    right -= 1
                    # to avoid duplicates
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                elif twosum >= target:
                    right -= 1
                else:
                    left += 1
        return answers
    
# # Alternate solution
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         dups = set()
#         answer = set()
#         seen = {}
#         for i, val1 in enumerate(nums):
#             if val1 not in dups:
#                 dups.add(val1)
#                 for j, val2 in enumerate(nums[i + 1:]):
#                     complement = - val1 - val2
#                     if complement in seen and seen[complement] == i:
#                         answer.add(tuple(sorted([val1, val2, complement])))
#                     seen[val2] = i
#         return answer                