class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            # Expand for odd-length palindromes (center is at i)
            len1 = self.expand_around_center(s, i, i)
            # Expand for even-length palindromes (center is between i and i+1)
            len2 = self.expand_around_center(s, i, i + 1)
            
            # Take the longest palindrome found from this center
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update our start and end indices
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring
        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Expand outward while within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the length of the palindrome
        # (Subtract 1 because the loop breaks when s[left] != s[right])
        return right - left - 1