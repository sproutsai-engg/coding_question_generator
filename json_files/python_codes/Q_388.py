##Question ID: 388

def length_longest_path(input: str) -> int:
    dir_length_stack = []
    max_file_length = 0
    lines = input.split('\n')

    for line in lines:
        level = line.count('\t')
        line = line.lstrip('\t')

        while len(dir_length_stack) > level:
            dir_length_stack.pop()

        if dir_length_stack:
            length = dir_length_stack[-1] + len(line) + 1
        else:
            length = len(line)
        dir_length_stack.append(length)

        if '.' in line:
            max_file_length = max(max_file_length, length)
            
    return max_file_length


## Structure
def length_longest_path(input: str) -> int:
    # Your code here

    pass