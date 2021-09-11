class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        a=len(str(self))
        if str(self)[0]=='-':
            return int(str(self)[:-a:-1])
        elif str(self)[a-1]=='0':
            return int(str(self)[-2:-(a+1):-1])
        else:
            c=str(self)[::-1]
            return int(c)
        '''
        if x==0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31<x<2**31-1:
            return x
        return 0