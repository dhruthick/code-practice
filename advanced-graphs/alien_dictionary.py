class Solution(object):
    '''
    269: HARD
    There is a new alien language that uses the English 
    alphabet. However, the order of the letters is 
    unknown to you.

    You are given a list of strings words from the 
    alien language's dictionary. Now it is claimed that 
    the strings in words are sorted lexicographically 
    by the rules of this new language.

    If this claim is incorrect, and the given 
    arrangement of string in words cannot correspond to 
    any order of letters, return "".

    Otherwise, return a string of the unique letters in 
    the new alien language sorted in lexicographically 
    increasing order by the new language's rules. If 
    there are multiple solutions, return any of them.
    '''
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Leetcode's solution

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
                    
        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
    

        # # MY SOLUTION
        # from collections import defaultdict
        
        # if len(words) == 1:
        #     return "".join(set([w for w in words[0]]))

        # all_letters = set()
        # adj_list = defaultdict(set)

        # # build adjacency list
        # for i in range(1, len(words)):
        #     word1, word2 = words[i - 1], words[i]
        #     j = 0
        #     while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
        #         all_letters.add(word1[j])
        #         j += 1
        #     break_point = j
        #     if j < len(word1) and j < len(word2):
        #         adj_list[word1[j]].add(word2[j])
        #     elif j >= len(word2) and j < len(word1):
        #         return ""
        #     while j < len(word1):
        #         all_letters.add(word1[j])
        #         j += 1
        #     while break_point < len(word2):
        #         all_letters.add(word2[break_point])
        #         break_point += 1  

        # # topological sorting to detect cycles
        # indegree = defaultdict(int)
        # for letters in adj_list.values():
        #     for l in letters:
        #         indegree[l] += 1
        
        # queue = [letter for letter in all_letters if indegree[letter] == 0]
        # ordered_letters = ""
        # while queue:
        #     letter = queue.pop(0)
        #     ordered_letters += letter
        #     for l in adj_list[letter]:
        #         indegree[l] -= 1
        #         if indegree[l] == 0:
        #             queue.append(l)

        # return ordered_letters if len(ordered_letters) == len(all_letters) else ""