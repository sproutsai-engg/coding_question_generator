##Question ID: 1702

def maximum_binary_string(binary: str) -> str:
    zero_count = binary.count('0')
    
    if zero_count <= 1:
        return binary
    
    one_count = len(binary) - zero_count

    result = "1" * one_count + "0" * (zero_count - 1) + "1####1"
    return result[:len(binary)]

## Structure
def maximum_binary_string(binary: str) -> str:
    # Your code here

    pass