class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS

        # itertools
        return list(itertools.permutations(nums))