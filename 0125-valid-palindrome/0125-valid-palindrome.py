import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        rev_s = low_s[::-1]
        if low_s == rev_s:
            return True
        else:
            return False
