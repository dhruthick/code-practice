class Solution:
    '''
    MEDIUM: 647
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.
    '''

    # time - O(n^2), space - O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0 

        for i in range(len(s)):
            res += self.middleLength(s,i, i)
            res += self.middleLength(s, i, i+1)

        return res
       
    def middleLength(self, s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res+=1
            l-=1
            r+=1
        return res

        