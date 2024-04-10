##Question ID: 339

from typing import List, Union

def depth_sum(nested_list: List[Union[int, List]]) -> int:
    def depth_sum_helper(nested_list: List[Union[int, List]], depth: int) -> int:
        return sum(element * depth if isinstance(element, int) else depth_sum_helper(element, depth + 1) for element in nested_list)

    return depth_sum_helper(nested_list, 1)


## Structure
from typing import List, Union
    # Your code here

    pass