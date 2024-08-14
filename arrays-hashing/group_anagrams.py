class Solution:
    '''
    MEDIUM: 49
    Given an array of strings strs, group the anagrams 
    together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters 
    of a different word or phrase, typically using all the original 
    letters exactly once.
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time - O(nklogk), Space - O(nk)
        # from collections import defaultdict
        # anagrams = defaultdict(list)
        # for word in strs:
        #     anagrams[''.join(sorted(word))].append(word)
        # return list(anagrams.values())

        # alternate approach, Time - O(nk), Space - O(nk)
        anagrams = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())