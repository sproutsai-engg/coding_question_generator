##Question ID: 157

def read4(buf4: List[str]) -> int:
    pass

def read(buf: List[str], n: int) -> int:
    total_read = 0
    buf4 = [''] * 4

    while total_read < n:
        read4_count = read4(buf4)
        for i in range(read4_count):
            if total_read < n:
                buf[total_read] = buf4[i]
                total_read += 1
            else:
                break
        if read4_count < 4:
            break

    return total_read

## Structure
def read4(buf4: List[str]) -> int:
    # Your code here

    pass