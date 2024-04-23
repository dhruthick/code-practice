class Solution(object):
    '''
    Given an array of non-negative integers arr, you are initially positioned 
    at start index of the array. When you are at index i, you can jump to 
    i + arr[i] or i - arr[i], check if you can reach any index with value 0.

    Notice that you can not jump outside of the array at any time.
    '''
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])

        return False