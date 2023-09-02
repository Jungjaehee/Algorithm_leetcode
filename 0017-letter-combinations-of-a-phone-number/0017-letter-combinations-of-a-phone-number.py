class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return

        letters = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], \
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], \
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'] }
    
        answer = []

        def dfs(point: int, string = ""):
            for i in range(point, len(digits)):
                for ch in letters[digits[i]]:
                    string += ch
                    dfs(i+1, string)
                    
                    if len(string) == len(digits):
                        answer.append(string)

                    string = string[:-1]

        point = 0
        dfs(0)

        return answer