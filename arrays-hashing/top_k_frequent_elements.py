class Solution:
    '''
    MEDIUM: 347
    Given an integer array nums and an integer k, 
    return the k most frequent elements. You may 
    return the answer in any order.
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time - O(nlogk), Space - O(n + k)
        hashmap = collections.Counter(nums)
        return heapq.nlargest(k, hashmap.keys(), key = hashmap.get)