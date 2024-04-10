##Question ID: 331

def is_valid_serialization(preorder: str) -> bool:
    nodes = preorder.split(',')
    node_count = 1

    for node in nodes:
        node_count -= 1
        if node_count < 0:
            return False
        if node != '#':
            node_count += 2

    return node_count == 0

## Structure
def is_valid_serialization(preorder: str) -> bool:
    # Your code here

    pass