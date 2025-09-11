class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        j = 0
        array = []
        binary = list(bin(n)[2:])
        for i in binary:
            array.append(int(i))
        while j < len(array):
            if array[j] == 1:
                x += 1
            j += 1
        return x
        