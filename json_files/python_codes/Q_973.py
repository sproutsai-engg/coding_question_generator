##Question ID: 973

def moves_to_stamp(stamp: str, target: str) -> list:
    result = []
    is_stamped = [False] * len(target)
    stamp_count = 0
    target = list(target)

    while stamp_count < 10 * len(target):
        found_stamp = False
        for i in range(len(target) - len(stamp) + 1):
            if is_stamped[i]:
                continue
            j = 0
            overlap = 0
            while j < len(stamp) and (target[i + j] == '?' or target[i + j] == stamp[j]):
                if target[i + j] == stamp[j]:
                    overlap += 1
                j += 1
            if j == len(stamp) and overlap > 0:
                for j in range(len(stamp)):
                    target[i + j] = '?'
                result.append(i)
                is_stamped[i] = True
                found_stamp = True
        if not found_stamp:
            break
        
        stamp_count += 1

    for c in target:
        if c != '?':
            return []

    return result[::-1]


## Structure
def moves_to_stamp(stamp: str, target: str) -> list:
    # Your code here

    pass