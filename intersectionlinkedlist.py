class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode( headA: ListNode, headB: ListNode) -> ListNode:
        d={}
        while(headA):
            d[id(headA)]=headA
            headA=headA.next
        while(headB):
            if id(headB) in d:
                  return headB
            headB=headB.next
        return None
print(Solution.getIntersectionNode(ListNode[2,6,4], ListNode[1,5]))