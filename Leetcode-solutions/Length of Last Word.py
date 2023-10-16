class Solution:
    def lengthOfLastWord(self, s):
        
        s=s.strip()
        last_index = len(s)-1
        counter=0
        for reverse in range(last_index,-1,-1): 
            if s[reverse]==" ":
                break
            counter +=1
        return counter
