class Solution:
    '''
    MEDIUM: 300
    Given an integer array nums, return the length of the longest strictly increasing 
    subsequence
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)


        