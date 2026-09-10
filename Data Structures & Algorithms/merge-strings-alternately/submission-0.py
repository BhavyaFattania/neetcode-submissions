class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        smaller_list = min(len(word1),len(word2))
        i=0
        while i < smaller_list:
            lst.append(word1[i])
            lst.append(word2[i])
            i+=1
        if i < len(word2):
            while i < len(word2):
                lst.append(word2[i])
                i+=1
        elif i < len(word1):
            while i < len(word1):
                lst.append(word1[i])
                i+=1
        return "".join(lst)
        