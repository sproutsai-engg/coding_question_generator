##Question ID: 141

def hasCycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

## Structure
def hasCycle(head):
    # Your code here

    pass