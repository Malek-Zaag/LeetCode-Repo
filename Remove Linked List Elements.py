""" class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      if head==None: return None
      prev=ListNode(-1)
      prev.next=head
      curr=prev
      while curr.next !=None:
        if curr.next.val==val:
          curr.next=curr.next.next
        else:
          curr=curr.next
      return prev.next """