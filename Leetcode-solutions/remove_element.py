class Solution:
    def removeElement(self,nums, val):
        c=0
        i=0
        x=0
        while i<len(nums):
            if nums[i]!=val:
                nums[x]=nums[i]
                x+=1
            i+=1
        return x
