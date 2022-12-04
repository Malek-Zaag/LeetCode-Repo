""" class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list1==None and list2==None: return None
      if list1==None: return list2
      if list2==None: return list1  
      res=curr=ListNode(0)
      curr1=list1
      curr2=list2
      while curr1 !=None and curr2!= None:
        if curr1.val <= curr2.val:
          curr.next=curr1
          curr1=curr1.next
        else :
          curr.next=curr2
          curr2=curr2.next
        curr=curr.next
      curr.next=curr1 or curr2
      return res.next """