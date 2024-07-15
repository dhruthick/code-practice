class Solution:
    '''
    HARD: 4
    Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    '''
    def findKthSmallest(self, a, b, k):
        a_start, a_end, b_start, b_end = 0, len(a) - 1, 0, len(b) - 1
        while True:
            if a_start > a_end:
                return b[k - a_start]
            if b_start > b_end:
                return a[k - b_start]
            a_mid, b_mid = (a_start + a_end) // 2, (b_start + b_end) // 2
            if a_mid + b_mid < k:
                if a[a_mid] < b[b_mid]:
                    a_start = a_mid + 1
                else:
                    b_start = b_mid + 1
            else:
                if a[a_mid] < b[b_mid]:
                    b_end = b_mid - 1
                else:
                    a_end = a_mid - 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2:
            return self.findKthSmallest(nums1, nums2, n // 2)
        return (self.findKthSmallest(nums1, nums2, n // 2) + self.findKthSmallest(nums1, nums2, n // 2 - 1)) / 2

        