# https://leetcode.com/problems/palindrome-linked-list/

import collections
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deque = collections.deque()
        if not head:
            return True

        node = head
        while node is not None:
            deque.append(node.val)
            node = node.next

        while len(deque) >= 2:
            if deque.popleft() != deque.pop():
                return False
        return True