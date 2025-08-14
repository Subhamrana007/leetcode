class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for values in operations:
            if values == "++X" or values == "X++":
                X +=1
            else:
                X -=1
        return X

        """
        :type operations: List[str]
        :rtype: int
        """
        