class Solution:
    def climbStairs(self, n,array={}):
        if n<=3:
            return n
        if n in array:
            return array[n]
        else:
            array[n-1]=self.climbStairs(n-1,array)
            return array[n-1]+self.climbStairs(n-2)
