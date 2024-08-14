class Solution:
    '''
    EASY: 217
    Given an integer array nums, return true if any value appears at 
    least twice in the array, and return false if every element is distinct.
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time - O(n), Space - O(n)
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
        # alternate time - O(nlogn), space - O(1) approach
        # sort and check adjacent elements