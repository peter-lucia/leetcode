class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flip = {'1':'0','0':'1'}
        test = ''
        for each in str(bin(num)[2:]):
            test += flip[each]
        return int(test, 2)
        