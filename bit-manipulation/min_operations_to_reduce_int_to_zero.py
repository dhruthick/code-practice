class Solution:
    '''
    MEDIUM: 2571
    You are given a positive integer n, you can do the following operation any number of times:

    Add or subtract a power of 2 from n.
    Return the minimum number of operations to make n equal to 0.

    A number x is power of 2 if x == 2i where i >= 0.
    '''
    def minOperations(self, n: int) -> int:
        # get the binary representation in a string
        binary = list(bin(n)[2:])
        i = len(binary) - 1
        # track the number of 1s encountered so far
        count = 0
        ans = 0
        while i >= 0:
            # if it is 1, increment count, set to zero, move on
            if binary[i] == '1':
                count += 1
                binary[i] = '0'
                i -= 1
            # if it is 0
            else:
                # if encountered only one 1, increment answer (subtraction),
                # reset count, move on
                if count == 1:
                    ans += 1
                    count = 0
                    i -= 1
                # if encountered more than one 1, increment answer (addition), 
                # reset count, set to 1, stay
                elif count > 1:
                    ans += 1
                    binary[i] = '1'
                    count = 0
                    continue
                # if no 1s are encountered, move on
                else:
                    i -= 1
        # finally one subtraction if a single 1 is encountered,
        # one addition and one subtraction if more than one 1 is encountered.
        if count > 0:
            ans += 1
        if count > 1:
            ans += 1     
        return ans