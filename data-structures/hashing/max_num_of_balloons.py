class Solution:
    '''
    EASY: 1189
    Given a string text, you want to use the characters 
    of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. 
    Return the maximum number of instances that can be formed.
    '''
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = ['b', 'a', 'l', 'o', 'n']
        count = {}
        for l in letters:
            count[l] = 0
            
        for c in text:
            if c in letters:
                count[c] += 1
        
        count['o'] //= 2
        count['l'] //= 2

        return min(count.values())
        