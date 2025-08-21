class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = list(word1)
        y = list(word2)
        empt_arr = []
        for i in range (max(len(x),len(y))):

            if i < len(x):
                empt_arr.append(x[i])
            if i < len(y):
                empt_arr.append(y[i])
        return "".join(empt_arr)
        