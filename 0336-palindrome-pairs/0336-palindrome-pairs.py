class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # Map each reversed word to its original index
        reversed_dict = {word[::-1]: i for i, word in enumerate(words)}
        res = set() # Use a set to prevent duplicate pairs
        
        for i, word in enumerate(words):
            n = len(word)
            
            # Try splitting the word at every possible index j
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: Prefix is a palindrome, we need to find reversed suffix in our dict
                if prefix == prefix[::-1]:
                    if suffix in reversed_dict and reversed_dict[suffix] != i:
                        res.add((reversed_dict[suffix], i))
                        
                # Case 2: Suffix is a palindrome, we need to find reversed prefix in our dict
                if suffix == suffix[::-1]:
                    if prefix in reversed_dict and reversed_dict[prefix] != i:
                        res.add((i, reversed_dict[prefix]))
                        
        return [list(p) for p in res]
        