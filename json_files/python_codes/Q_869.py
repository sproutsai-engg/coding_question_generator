##Question ID: 869

def is_similar(a: str, b: str) -> bool:
    diff_count = 0
    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            diff_count += 1
            if diff_count > 2:
                return False
    return True

def count_groups(strs: list[str]) -> int:
    count = 0
    visited = [False] * len(strs)
    for i in range(len(strs)):
        if not visited[i]:
            count += 1
            visited[i] = True
            for j in range(i + 1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    visited[j] = True
    return count


## Structure
def is_similar(a: str, b: str) -> bool:
    # Your code here

    pass