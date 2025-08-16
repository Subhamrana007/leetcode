class Solution(object):
    def maximum69Number (self, num):
        str_num = str(num)
        largest_number = str_num.replace("6","9",1)
        largest_int = int(largest_number)
        return largest_int
        """
        :type num: int
        :rtype: int
        """
        