##Question ID: 364

from typing import List, Union

NestedInteger = Union[int, List[Union[int, "NestedInteger"]]]

def depthSumInverse(nestedList: List[NestedInteger]) -> int:
    max_depth = max_depth_helper(nestedList)
    return sum_helper(nestedList, max_depth)

def max_depth_helper(nested_list: List[NestedInteger]) -> int:
    depth = 1
    for nested in nested_list:
        if isinstance(nested, list):
            depth = max(depth, 1 + max_depth_helper(nested))
    return depth

def sum_helper(nested_list: List[NestedInteger], depth: int) -> int:
    sum = 0
    for nested in nested_list:
        if isinstance(nested, int):
            sum += depth * nested
        else:
            sum += sum_helper(nested, depth - 1)
    return sum

## Structure
from typing import List, Union
    # Your code here

    pass