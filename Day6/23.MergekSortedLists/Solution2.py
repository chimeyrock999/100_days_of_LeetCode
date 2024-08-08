
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode: 
        merged = ListNode()
        curr = merged
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        while list1:
            curr.next = list1
            curr = list1
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = list2
            list2 = list2.next

        return merged.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = int(len(lists)/2)
        return self.merge(self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:]))   