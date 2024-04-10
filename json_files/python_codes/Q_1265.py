##Question ID: 1265

def printLinkedListInReverse(head: 'ImmutableListNode') -> None:
    if head is not None:
        printLinkedListInReverse(head.getNext())
        head.printValue()

## Structure
def printLinkedListInReverse(head: 'ImmutableListNode') -> None:
    # Your code here

    pass