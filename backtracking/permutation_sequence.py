class Solution:
    '''
    HARD: 60
    The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.
    '''
    def backtrack(self, num, num_list):
        if not num_list:
            self.k -= 1
            if not self.k:
                self.answer = num
            return
        for i in range(len(num_list)):
            self.backtrack(num + num_list[i], num_list[:i] + num_list[i + 1:])
            if not self.k:
                return


    def getPermutation(self, n: int, k: int) -> str:
        self.k = k
        self.answer = None
        self.backtrack('', [str(i) for i in range(1, n + 1)])
        return self.answer
        