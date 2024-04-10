##Question ID: 24

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    second = head.next
    head.next = swapPairs(second.next)
    second.next = head

    return second

## Structure
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    # Your code here

    pass