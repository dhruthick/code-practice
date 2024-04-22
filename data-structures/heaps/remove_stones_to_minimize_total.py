class Solution:
    '''
    MEDIUM: 1962
    You are given a 0-indexed integer array piles, where piles[i] represents 
    the number of stones in the ith pile, and an integer k. You should apply 
    the following operation exactly k times:

        Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

    Notice that you can apply the operation on the same pile more than once.

    Return the minimum possible total number of stones remaining after 
    applying the k operations.

    floor(x) is the greatest integer that is smaller than or equal to x 
    (i.e., rounds x down).
    '''
    def minStoneSum(self, piles: List[int], k: int) -> int:
        from heapq import heapify, heappush, heappop
        piles = [-x for x in piles]
        heapify(piles)
        while k:
            heappush(piles, heappop(piles) // 2)
            k -= 1
        return - sum(piles)