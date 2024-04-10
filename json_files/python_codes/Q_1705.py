##Question ID: 1705

def unhappyFriends(n, preferences, pairs):
    pair_mapping = [0] * n
    for pair in pairs:
        pair_mapping[pair[0]] = pair[1]
        pair_mapping[pair[1]] = pair[0]

    unhappy_count = 0
    for x in range(n):
        y = pair_mapping[x]
        pref_x = preferences[x]
        idx_y = pref_x.index(y)

        for i in range(idx_y):
            u = pref_x[i]
            v = pair_mapping[u]
            pref_u = preferences[u]
            if x in pref_u[:pref_u.index(v)]:
                unhappy_count += 1
                break

    return unhappy_count // 2


## Structure
def unhappyFriends(n, preferences, pairs):
    # Your code here

    pass