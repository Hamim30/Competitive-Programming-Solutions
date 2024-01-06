class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for k in nums:
            if k in dict:
                dict[k]+=1
            else:
                dict[k]=1
        x=0
        y=0
        print(dict)
        for k,v in dict.items():
            if v >y:
                x=k
                y=v
               
        return x
