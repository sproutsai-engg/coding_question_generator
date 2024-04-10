##Question ID: 1267

def remove_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current:
        sum = 0
        while head:
            sum += head.val
            if sum == 0:
                current.next = head.next
            head = head.next
        current = current.next
        if current:
            head = current.next

    return dummy.next


## Structure
def remove_zero_sum_sublists(head):
    # Your code here

    pass