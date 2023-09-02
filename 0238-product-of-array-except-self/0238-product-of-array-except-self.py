from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        N = len(nums)
        p = 1
        ## 왼쪽 곱 / 오른쪽 곱
        for i in range(N):
            answer.append(p)
            p = p*nums[i]

        p = 1
        for i in range(N-1, -1, -1):
            answer[i] *= p
            p = p * nums[i]

        return answer
        # N = len(nums)
        # nums_extend = nums + nums
        # mul_nums = []

        # for i in range(N):
        #     mul_nums.append(reduce(lambda x, y:x*y, nums_extend[i+1:i+N]))
        #     # mul_nums = mul_nums * np.array(nums_extend[i:i+N])
        #     # mul_nums.append(eval(('*').join(map(str, nums_extend[i+1:i+N]))))

        # return mul_nums
        
        # answer = []
        # p = 1
        # for i in range(len(nums)):
        #     res = nums[:i]+nums[i+1:]
        #     res = ('*').join(map(str,res))
        #     answer.append(eval(res))

        # return answer