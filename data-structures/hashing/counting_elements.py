class Solution:
    '''
    EASY: 1426
    Given an integer array arr, count how many elements 
    x there are, such that x + 1 is also in arr. 
    If there are duplicates in arr, count them separately.
    '''
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        ans = 0
        for x in arr:
            if x + 1 in nums:
                ans += 1
        return ans