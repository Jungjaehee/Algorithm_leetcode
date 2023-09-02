import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_eng = re.sub("[^a-zA-Z]", " ", paragraph).lower() + " "

        for e in banned:
            paragraph_eng = paragraph_eng.replace(e.lower()+" ", " ")
    
        word_list = paragraph_eng.split()

        word_set = set(word_list)

        max_cnt = 0
        common_word = ""
        for w in word_set:
            cnt = word_list.count(w)
            if cnt > max_cnt:
                max_cnt = cnt
                common_word = w

        return common_word
