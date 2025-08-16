class Solution(object):
    def maximum69Number (self, num):
        str_num = str(num)
        largest_num = int(str_num.replace("6","9",1))

        return (largest_num)

        """
        :type num: int
        :rtype: int
        """
        