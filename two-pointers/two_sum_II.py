class Solution(object):
    '''
    167: MEDIUM
    Two sum but the input array is sorted and needs
    to be done within O(1) space
    '''
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # naive approach - time limit exceed
        # # answer = []
        # # for i1 in range(len(numbers)-1):
        # #     i2 = i1 + 1
        # #     while i2 < len(numbers) and numbers[i2] <= target - numbers[i1]:
        # #         if numbers[i2] == target - numbers[i1]:
        # #             answer.extend([i1 + 1, i2 + 1])
        # #             return answer
        # #         i2 += 1

        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

                