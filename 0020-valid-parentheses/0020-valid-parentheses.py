class Solution:
    def isValid(self, s: str) -> bool:
        open_s = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 or s[i] in open_s:
                stack.append(s[i])
                continue

            item = stack.pop()
            if  item not in open_s or s[i] != open_s[item]:
                return False

        if len(stack) != 0:
            return False
        return True