class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        count = 1
        empt_arr = list()
        
        while a < A and b < B:
            if count == 1:
                empt_arr.append(word1[a])
                a += 1
                count = 2
            else:
                empt_arr.append(word2[b])
                b +=1
                count = 1
        

        while a < A:
            empt_arr.append(word1[a])
            a +=1
        
        while b < B:
            empt_arr.append(word2[b])
            b +=1
        
        return "".join(empt_arr)

        