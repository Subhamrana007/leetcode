class Solution(object):
    def fizzBuzz(self, n):
        emt_list=list()
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                emt_list.append("FizzBuzz")
            elif i % 3==0 :
                emt_list.append('Fizz')
            elif i % 5==0:
                emt_list.append('Buzz')
            else: 
                emt_list.append(str(i))
        return emt_list
    

        """
        :type n: int
        :rtype: List[str]
        """
        