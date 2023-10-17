
class Solution:
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        x=head
        y=head.next
        while y!=None:
            if x.val<y.val:
                x=x.next
                y=y.next
            else:
                x.next=y.next
                y=y.next
        return head
