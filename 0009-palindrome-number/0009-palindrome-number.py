class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        word = str(x)
        inverted = word[::-1]

        if inverted == word:
            return True
        else:
            return False


        