class Solution:
    '''
    MEDIUM: 2952
    You are given a 0-indexed integer array coins, representing the values 
    of the coins available, and an integer target.

    An integer x is obtainable if there exists a subsequence of coins that 
    sums to x.

    Return the minimum number of coins of any value that need to be added 
    to the array so that every integer in the range [1, target] is 
    obtainable.

    A subsequence of an array is a new non-empty array that is formed 
    from the original array by deleting some (possibly none) of the 
    elements without disturbing the relative positions of the remaining 
    elements.
    '''
    def minimumAddedCoins(self, nums: List[int], target: int) -> int:
        nums.sort()
        current_max = 0
        additions = 0
        index = 0

        while current_max < target:
            if index < len(nums) and nums[index] <= current_max + 1:
                current_max += nums[index]
                index += 1
            else:
                current_max += current_max + 1
                additions += 1

        return additions