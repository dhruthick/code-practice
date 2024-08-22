class Solution:
    '''
    MEDIUM: 139
    Given a string s and a dictionary of strings wordDict, return true 
    if s can be segmented into a space-separated sequence of one or 
    more dictionary words.

    Note that the same word in the dictionary may be reused 
    multiple times in the segmentation.
    '''
    # time - O(nmk), n - len(s), m - len(wordDict), k - avg. lenght of word
    # space - O(n)
    @lru_cache(None)
    def backtrack(self, string_left):
        if not string_left:
            return True
        for w in self.words:
            if string_left[:len(w)] == w and self.backtrack(string_left[len(w):]):
                return True
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self. words = wordDict
        return self.backtrack(s)

        

        