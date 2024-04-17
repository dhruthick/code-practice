class Solution:
    '''
    EASY: 383
    Given two strings ransomNote and magazine, return true if 
    ransomNote can be constructed by using the letters from 
    magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
    '''
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Time complexity: O(M+N)  where M is number of letters in magazine and N is number of letters in ransomNote
        # Space complexity: O(M)
        
        letters = {}
        for c in magazine:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        for d in ransomNote:
            if d in letters and letters[d] != 0:
                letters[d] -= 1
            else:
                return False
        
        return True  