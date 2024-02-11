class Solution(object):
    '''
    128 : MEDIUM
    Given an unsorted array of integers nums, return the
    length of the longest consecutive elements sequence.
    
    You must write an algorithm that runs in O(n) time.
    '''
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # convert the list to set (Hashset) 
        # O(1) lookups in sorted manner is then possible
        nums = set(nums)
        answer = 0
        for n in nums:
            # follow the brute force approach but only when necessary.
            if n - 1 not in nums:
                curr = n
                curr_ans = 1

                while curr + 1 in nums:
                    curr_ans += 1
                    curr += 1

                answer = max(answer, curr_ans)
        return answer