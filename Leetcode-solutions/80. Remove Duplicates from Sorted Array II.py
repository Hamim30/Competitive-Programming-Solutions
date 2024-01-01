class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first=nums[0]
        c=0
        swap=0
        k=len(nums)
        for i in range(len(nums)):
            print(swap)
            if nums[i]==first and c<2 and i==swap:
                c+=1
                swap+=1
            elif nums[i]==first and c<2 and i!=swap:
                nums[swap]=first
                swap+=1
                c+=1
            elif nums[i]==first and c==2:
                k-=1
            elif nums[i]!=first and c<=2 and i==swap:
                first=nums[i]
                c=1
                swap+=1
            elif nums[i]!=first and c<=2 and i!=swap:
                first=nums[i]
                nums[swap]=first
                swap+=1
                c=1
        return k

                

        
            


            

        
