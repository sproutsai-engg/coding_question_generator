##Question ID: 401

def readBinaryWatch(turnedOn: int):
    def count_bits(n):
        return bin(n).count('1')

    times = []
    for h in range(12):
        for m in range(60):
            if count_bits(h) + count_bits(m) == turnedOn:
                times.append(f"{h}:{m:02d}")
    return times

## Structure
def readBinaryWatch(turnedOn: int):
    # Your code here

    pass