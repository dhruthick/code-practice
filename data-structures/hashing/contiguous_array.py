class Solution:
    '''
    MEDIUM: 525
    Given a binary array nums, return the maximum length of 
    a contiguous subarray with an equal number of 0 and 1.
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        count_index = {
            0: -1
        }
        # increment when 1, decrement when 0
        count = 0
        ans = 0
        # track the first index a count value occurs and use it later
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in count_index:
                ans = max(ans, i - count_index[count])
            else:
                count_index[count] = i
        return ans