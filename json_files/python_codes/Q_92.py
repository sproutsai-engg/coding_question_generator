##Question ID: 92

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next
    cur = pre.next
    for _ in range(left, right):
        t = cur.next
        cur.next = t.next
        t.next = pre.next
        pre.next = t
    return dummy.next

## Structure
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # Your code here

    pass