""" class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head==None : return None
      if head.next==None: return head
      cur = head
      while cur:
          while cur.next and cur.next.val == cur.val:
              cur.next = cur.next.next     # skip duplicated node
          cur = cur.next     # not duplicate of current node, move to next node
      return head """