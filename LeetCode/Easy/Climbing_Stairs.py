'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        n0 = 0
        n1 = 1
        for i in range(n):
            res = n0 + n1
            n0 = n1
            n1 = res
        return res