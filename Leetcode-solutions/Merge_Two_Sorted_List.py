class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(None)
        head=dummy
        while list1 and list2:
            if list1.val<list2.val:
                dummy.next=list1
                list1=list1.next
            else:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        dummy.next=list1 or list2
        return head.next
