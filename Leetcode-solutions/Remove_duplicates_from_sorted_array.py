class Solution:
    def removeDuplicates(self, nums):
        c=1
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[c]=nums[i]
                c+=1
        return c
        
