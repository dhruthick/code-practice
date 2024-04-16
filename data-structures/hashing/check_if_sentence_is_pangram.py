class Solution:
    '''
    EASY: 1832
    A pangram is a sentence where every letter of the 
    English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, 
    return true if sentence is a pangram, or false otherwise.
    '''
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for l in sentence:
            letters.add(l)
        return len(letters) == 26