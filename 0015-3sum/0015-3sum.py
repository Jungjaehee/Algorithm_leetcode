class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        zero_nums = set()

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                res_sum = nums[i] + nums[left] + nums[right]
                if res_sum == 0:
                    zero_nums.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif res_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(map(list, list(zero_nums)))
        