class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number = []
        string = []

        for l in logs:
            if ('').join(l.split()[1:]).isalpha():
                string.append(tuple(((' ').join(l.split()[1:]), l)))
            else:
                number.append(l)

        string.sort(key=lambda x:(x[0], x[1]))

        final_log = [x[1] for x in string]
        final_log.extend(number)

        return final_log