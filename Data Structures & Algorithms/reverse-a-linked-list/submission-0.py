class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        perv=None
        while curr:
            temp=curr.next
            curr.next=perv
            perv=curr
            curr=temp
        return perv