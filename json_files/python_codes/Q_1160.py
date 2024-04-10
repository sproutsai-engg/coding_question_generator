##Question ID: 1160

def num_tile_possibilities(tiles: str) -> int:
    freq = [0] * 26
    for c in tiles:
        freq[ord(c) - ord('A')] += 1

    def dfs(freq):
        result = 0
        for i in range(26):
            if freq[i] > 0:
                freq[i] -= 1
                result += 1 + dfs(freq)
                freq[i] += 1
        return result

    return dfs(freq)

## Structure
def num_tile_possibilities(tiles: str) -> int:
    # Your code here

    pass