##Question ID: 722

def removeComments(self, source: List[str]) -> List[str]:
    result = []
    buffer = []
    in_block_comment = False

    for line in source:
        i = 0
        while i < len(line):
            if in_block_comment:
                if i < len(line) - 1 and line[i] == '*' and line[i + 1] == '/':
                    in_block_comment = False
                    i += 1
            else:
                if i < len(line) - 1 and line[i] == '/' and line[i + 1] == '*':
                    in_block_comment = True
                    i += 1
                elif i < len(line) - 1 and line[i] == '/' and line[i + 1] == '/':
                    break
                else:
                    buffer.append(line[i])
            i += 1

        if not in_block_comment and buffer:
            result.append(''.join(buffer))
            buffer.clear()

    return result


## Structure
def removeComments(self, source: List[str]) -> List[str]:
    # Your code here

    pass