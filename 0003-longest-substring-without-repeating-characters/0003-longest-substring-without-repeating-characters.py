class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_dict = collections.OrderedDict()
        
        for char in s:
            if char in char_dict:
                max_len = max(max_len, len(char_dict))
                key_list = list(char_dict.keys())
                for k in key_list:
                    char_dict.pop(k)
                    if k == char: break
                    
            char_dict[char] = 0
        

        return max(max_len, len(char_dict))