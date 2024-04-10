##Question ID: 807

def custom_sort_string(order, s):
    return ''.join(sorted(s, key=lambda x: order.index(x) if x in order else len(order)))


## Structure
def custom_sort_string(order, s):
    # Your code here

    pass