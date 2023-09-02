class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [ ('').join(sorted(w)) for w in strs ]
        set_strs = set(sorted_strs)
        
        result_list = []

        for w in set_strs:
            result_list.append([ strs[i] for i, s in enumerate(sorted_strs) if s == w ])
        
        return result_list
