#https://leetcode.com/problems/binary-search/?envType=study-plan&id=binary-search-i
class Solution:
    def search(self, array,element):     
        start =0
        end =len(array)-1
        
        while start<=end:
            mid = int((start+end)/2)
            if array[mid]==element:
                return mid
            else:
                if array[mid]<element:
                    start=mid+1
                else:
                    end =mid-1
        return -1
