class Solution:
    '''
    MEDIUM: 167
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
    find two numbers such that they add up to a specific target number. Let these two numbers be 
    numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array 
    [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same 
    element twice.

    Your solution must use only constant extra space.
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1

        while start < end:
            s = numbers[start] + numbers[end]

            if s < target:
                start+=1
            elif s > target:
                end-=1
            else:
                return [start+1, end+1]
        
        return []