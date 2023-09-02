class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ""

        if len(s) < 2 or s ==s[::-1]:
            return s

        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if max_len < j-i:
                        max_len = j-i
                        max_str = s[i:j]
                        break

        return max_str