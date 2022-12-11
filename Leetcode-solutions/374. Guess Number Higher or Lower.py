#https://leetcode.com/problems/guess-number-higher-or-lower/description/
class Solution:
    def guessNumber(self, n):    
        start =0
        end = n   
        while start<= end:
            mid =int((start+end)/2)
            if guess(mid)==-1:
                end=mid-1
            elif guess(mid)==1:
                start=mid+1
            elif guess(mid)==0:
                return mid
