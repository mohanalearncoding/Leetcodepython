class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeTwoLists( l1: ListNode, l2: ListNode) -> ListNode:
             if l1 is None:
                 return l2
             if l2 is None:
                 return l1
             if l1.val<l2.val:
                 l1.val=mergeTwoLists(l1.next,l2)
                 return l1
             if l2.val<l1.val:
                 l2.val=mergeTwoLists(l1,l2.next)
                 return l2
print(mergeTwoLists([1,2,4],[1,3,4]))