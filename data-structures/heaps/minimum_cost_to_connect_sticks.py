class Solution:
    '''
    MEDIUM: 1167
    You have some number of sticks with positive integer lengths. 
    These lengths are given as an array sticks, where sticks[i] is 
    the length of the ith stick.

    You can connect any two sticks of lengths x and y into one stick 
    by paying a cost of x + y. You must connect all the sticks until 
    there is only one stick remaining.

    Return the minimum cost of connecting all the given sticks into one 
    stick in this way.
    '''
    def connectSticks(self, sticks: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        heapify(sticks)
        total_cost = 0
        n = len(sticks) - 1
        while n:
            cost = heappop(sticks) + heappop(sticks)
            heappush(sticks, cost)
            total_cost += cost
            n -= 1
        return total_cost