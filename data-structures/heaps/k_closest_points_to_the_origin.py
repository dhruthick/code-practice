class Solution(object):
    '''
    MEDIUM: 973
    Given an array of points where points[i] = [xi, yi] represents 
    a point on the X-Y plane and an integer k, return the k closest 
    points to the origin (0, 0).

    The distance between two points on the X-Y plane is the 
    Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed 
    to be unique (except for the order that it is in).
    '''
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance_from_origin(x, y):
            return (x ** 2 + y ** 2) ** 0.5
        
        # # alternate approach, which is better?
        #
        # from heapq import heappush, heappop
        # distances = [(distance_from_origin(point[0], point[1]), point) for point in points]
        # heapify(distances)
        # answer = []
        # while k:
        #     answer.append(heappop(distances)[1])
        #     k -= 1
        # return answer

        heap = []
        size = 0
        for point in points:
            heappush(heap, (- distance_from_origin(point[0], point[1]), point))
            size += 1
            if size > k:
                heappop(heap)
                size -= 1
        return [point for _, point in heap]
