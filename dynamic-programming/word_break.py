class Solution:
    '''
    MEDIUM: 139
    Given a string s and a dictionary of strings wordDict, return true 
    if s can be segmented into a space-separated sequence of one or 
    more dictionary words.

    Note that the same word in the dictionary may be reused 
    multiple times in the segmentation.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        min_len = min([len(w) for w in wordDict])
        @lru_cache(None)
        def check_sentence(sent):
            # base cases
            if len(sent) == 0:
                return True
            if len(sent) < min_len:
                return False
            # iterable recurrence relation
            for word in wordDict:
                if len(sent) >= len(word) and sent[:len(word)] == word:
                    if check_sentence("" if len(word) == len(sent) else sent[len(word):]):
                        return True
            return False
            
        return check_sentence(s)

        

        