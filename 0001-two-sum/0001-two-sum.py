class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for idx, n in enumerate(nums):
            if target-n in nums_dict:
                return [nums_dict[target-n], idx]
            nums_dict[n] = idx
        
        '''
        for idx, n in enumerate(nums):
            res = target - n
            if res in nums[idx+1:]:
                return [idx, nums[idx+1:].index(res)+idx+1]
        '''
        '''
        for idx, n in enumerate(nums):
            try:
                res = nums[idx+1:].index(target-n) + idx + 1
            except ValueError:
                continue
            else:
                return [idx, res]
        '''        