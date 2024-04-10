##Question ID: 1333

def sort_based_on_mapping(mapping, nums):
    def mapped_value(num):
        return int(''.join(str(mapping[int(d)]) for d in str(num)))
    
    return sorted(nums, key=mapped_value)

## Structure
def sort_based_on_mapping(mapping, nums):
    # Your code here

    pass